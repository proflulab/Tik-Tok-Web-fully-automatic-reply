'''
Author: 杨仕明 shiming.y@qq.com
Date: 2024-08-24 09:14:32
LastEditors: 杨仕明 shiming.y@qq.com
LastEditTime: 2024-08-24 09:27:29
FilePath: /Tik-Tok-Web-fully-automatic-reply/src/browser/get_comments.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def create_chrome_driver():  # 打开浏览器
    options = Options()
    options.add_argument("--start-maximized")  # 启动时最大化窗口
    return webdriver.Chrome(options=options)  # 默认使用chromedriver的系统路径


chrome = create_chrome_driver()


def get_comments():  # 获取用户在抖音直播间发送的信息
    last_data_id = None  # 用于存储上一个 `data-id`

    try:
        while True:
            try:
                # 确保页面元素加载完成
                web_text_elements = WebDriverWait(chrome, 10).until(
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

                        # 这段代码用于判断是否是我的机器人发送的回复，防止信息被录入
                        if is_robot_reply(comment, 4):  # 前面一个变量是用户评论，后面是最多向上查找数量
                            continue  # 跳过该条记录

                        # 将新数据作为新行添加到 data_list 中
                        data_list.append([username, comment, "", ""])

                        # 打印用户名和评论
                        # print(f"用户名: {username} | 评论: {comment}")
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
