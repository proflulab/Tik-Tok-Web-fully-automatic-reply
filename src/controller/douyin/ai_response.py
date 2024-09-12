'''
Author: 杨仕明 shiming.y@qq.com
Date: 2024-08-30 22:32:42
LastEditors: 杨仕明 shiming.y@qq.com
LastEditTime: 2024-09-01 02:44:46
FilePath: /Tik-Tok-Web-fully-automatic-reply/src/controller/douyin/ai_response.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

from src.service.coze import CozeChatService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

from dotenv import load_dotenv
load_dotenv()

COZE_BOT_ID = os.getenv('COZE_BOT_ID') or '7368796970410459174'
COZE_AUTH = os.getenv('COZE_AUTH') or '*****'

Send_Message = os.getenv('COZE_AUTH') or False


def ai_response():  # 获取用户在抖音直播间发送的信息

    while True:
        # 查询 question_time 最小且 question_judgment 为空的一条数据
        query = """
        SELECT *
        FROM scores
        WHERE question_judgment = 1 AND (answer_content IS NULL OR answer_content = '')
        ORDER BY question_time ASC
        LIMIT 1;
        """

        from main import db

        result = db.fetch_all(query)

        if result:
            print("The record with the minimum question_time and a NULL question_judgment is:")
            print(result)

            bot_id = COZE_BOT_ID
            user_id = "12345678978976"
            api_token = COZE_AUTH

            coze_service = CozeChatService(bot_id, user_id, api_token)

            # Send a message and get the reply
            try:
                response = coze_service.send_and_get_reply(result[0][3])
                print("Full Conversation Response:")
                # print(response)
                # 更新表中的数据
                table_name = "scores"
                set_columns = {"answer_content": response[0]}
                conditions = {"id": result[0][0]}
                # 调用 update 方法
                db.update(table_name, set_columns, conditions)

                # from src.controller.douyin.get_comments import remove_non_bmp_characters
                # response_clear = remove_non_bmp_characters("Hello 😊 你好")
                # print(response_clear)
                # 将回复发送到抖音
                send_message(response)

            except Exception as e:
                print(f"An error occurred: {e}")

        else:
            print("No records found with answer_content as NULL.")
            time.sleep(1)

        # 关闭数据库连接
        # db.close_connection()


def send_message(message):  # 向抖音直播间发送信息
    """发送指定的消息并按下 Enter 键"""
    if Send_Message:
        try:
            from main import wrapper
            try:
                # 等待文本区域元素加载并找到
                text_element = WebDriverWait(wrapper.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//textarea[@class="webcast-chatroom___textarea"]'))
                )
                text_element.clear()
                text_element.send_keys(message)
                time.sleep(0.5)

                # 按下 Enter 键发送消息
                text_element.send_keys(Keys.RETURN)
            except Exception as e:
                print(f"发送消息时发生错误: {e}")
        except Exception as e:
            print(f"在发送信息时,导入网站信息发生错误: {e}")
