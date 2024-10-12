'''
Author: 杨仕明 shiming.y@qq.com, 宋明轩 songmingxuan936@gmail.com
Date: 2024-08-24 09:14:32
LastEditors: 宋明轩 songmingxuan936@gmail.com
LastEditTime: 2024-09-16 20:30:54
FilePath: /Tik-Tok-Web-fully-automatic-reply/src/controller/douyin/get_comments.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.controller.browser.selenium_driver import SeleniumWrapper

# from src.service.db.sqlite import SQLiteHelper

import os
import uuid

import re

from dotenv import load_dotenv
load_dotenv()

# db = SQLiteHelper("src/public/db_data/data.db")
# db.create_connection()

DOUYIN_URL = os.getenv('DOUYIN_URL') or 'https://www.douyin.com/'
DOUYIN_LIVE_URL = os.getenv('DOUYIN_LIVE_URL') or 'https://live.douyin.com/'
DOUYIN_ROOM = os.getenv('DOUYIN_ROOM') or '53417358783'

data_list = []  # 这里定义一个全局变量来存储数据


def remove_non_bmp_characters(text):  # 删除特殊符号的符号，以防万一发送不出去报错
    return ''.join(c for c in text if ord(c) <= 0xFFFF)


def is_robot_reply(comment, max_check_count):
    try:
        # 从最底往下上查找 answer_content 不为空值并且同时向上寻找三条
        query = """
        SELECT answer_content
        FROM scores
        WHERE answer_content IS NOT NULL AND answer_content != ''
        ORDER BY question_time DESC
        LIMIT ?;
        """

        from main import db

        # 将结果中的内容存储到一个列表中
        result_list = [row[0] for row in db.fetch_all(query, (max_check_count,))]
        # result_list = db.fetch_all(query)
        # print(result_list)

        comment = re.sub(r'^@[^,]+,\s*', '', comment)

        if comment in result_list:
            print('与机器人回复匹配项相同')
            return True
        else:
            print('未找到与机器人回复匹配项')
            return False

    except Exception as e:
        print(f"判断是否是机器人回复出现错误: {e}")


def get_comments():  # 获取用户在抖音直播间发送的信息
    last_data_id = None  # 用于存储上一个 `data-id`

    try:
        wrapper = SeleniumWrapper("DOUYIN", headless=False)
        wrapper.open_url(DOUYIN_LIVE_URL + DOUYIN_ROOM)
        # input("等待登录认证验证操作，按任意键继续！")

        # 检测 cookie 登陆文件是否失效
        if wrapper.check_login_status():
            print("登录状态正常，准备获取页面元素")

        while True:
            try:
                # 确保页面元素加载完成
                web_text_elements = WebDriverWait(wrapper.driver, 10).until(
                    EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR, 'div.webcast-chatroom___item.webcast-chatroom___enter-done'))
                )

                if web_text_elements:
                    # 提取最新的元素
                    latest_element = web_text_elements[-1]

                    # 获取当前元素的 `data-id`
                    current_data_id = latest_element.get_attribute('data-id')

                    # 如果 `data-id` 与上一个相同，则跳过
                    if current_data_id == last_data_id:
                        time.sleep(0.2)  # 等待一段时间后再次检查
                        continue

                    # 更新 `last_data_id`
                    last_data_id = current_data_id

                    try:
                        # 尝试获取用户名
                        username_element = latest_element.find_element(By.CSS_SELECTOR, '.u2QdU6ht')
                        username_text = username_element.text

                        # 尝试获取评论
                        comment_element = latest_element.find_element(By.CSS_SELECTOR, '.WsJsvMP9')
                        comment = comment_element.text

                        # 如果子项有 lEfJhurR 类别，则跳过,这里防止送礼物的信息被录入
                        if comment_element.find_elements(By.CSS_SELECTOR, '.lEfJhurR'):
                            continue

                        # 检查用户名最后一个字符是否为 `：`，如果不是则跳过，防止直播间进入消息提示
                        if not username_text.endswith('：'):
                            continue
                        # 去掉用户名中的最后一个字符 `：`
                        username = username_text[:-1]  # 移除最后一个字符 `：`

                        # 抖音暂时删除了"我"的标识--后续再说
                        # # 检查 .u2QdU6ht 元素中是否包含 .N3OGoGnA 子元素 ##查看是否是'我'发送的信息##
                        # if username_element.find_elements(By.CSS_SELECTOR, '.N3OGoGnA'):
                        #     if is_robot_reply(comment, 4):
                        #         continue
                        #     else:
                        #         print("这条信息不是机器人发送的")

                        if is_robot_reply(comment, 4):
                            continue
                        else:
                            print("这条信息不是机器人发送的")

                        # 将新数据作为新行添加到 data_list 中
                        data_list.append([username, comment, "", ""])

                        # 打印用户名和评论
                        print(f"用户名: {username} | 评论: {comment}")

                        # 生成唯一的 UUID
                        unique_id = str(uuid.uuid4())

                        from main import db
                        sql_text = "INSERT INTO scores VALUES(?, ?, ?, ?, ?, ?, ?)"
                        db.execute_query(sql_text, (unique_id, username, time.time(), comment, '', '', ''))

                    except Exception as inner_e:
                        # 如果在尝试获取用户名或评论时出错，继续到下一个元素
                        print("## 提取信息时发生错误，可能是没找到类别，不用在意，可以查看这段代码的位置进行调试 ##")  # 防止一些非信息元素出bug
                        inner_e = inner_e  # 这段变量没有任何用处，只是防止报错，如果要调试，可以删除这段代码
                        # print(f"提取信息时发生错误: {inner_e}")  # 调试使用
                        continue

                else:
                    print("没有找到发言元素")

            except Exception as e:
                print(f"监控公屏时发生错误: {e}")

            # 等待一段时间后再次检查
            time.sleep(1)  # 可以根据需要调整检查间隔

    except Exception as e:
        print(f"监控公屏时发生错误: {e}")
