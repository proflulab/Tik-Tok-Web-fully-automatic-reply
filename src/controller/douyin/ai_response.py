'''
Author: 杨仕明 shiming.y@qq.com, 宋明轩 songmingxuan936@gmail.com
Date: 2024-08-30 22:32:42
LastEditors: 宋明轩 songmingxuan936@gmail.com
LastEditTime: 2024-09-17 22:24:53
FilePath: /Tik-Tok-Web-fully-automatic-reply/src/controller/douyin/ai_response.py
Description:

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved.
'''

from src.service.coze import CozeChatService
from src.controller.browser.selenium_driver import SeleniumWrapper
from src.controller.douyin.get_comments import remove_non_bmp_characters
import time
import os

from dotenv import load_dotenv
load_dotenv()

COZE_BOT_ID = os.getenv('COZE_BOT_ID') or '7368796970410459174'
COZE_AUTH = os.getenv('COZE_AUTH') or '*****'

# 没有环境变量 SEND_MESSAGE 的时候返回 False，如果有这个变量，根据其内容返回布尔值
Send_Message = os.getenv('SEND_MESSAGE', 'False').lower() == 'true'


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
                # print(f"Customer service robot reply : {response}")

                # 将回复发送到抖音
                if Send_Message:
                    # 将 response 拼接成 "@username，response" 格式
                    response_sent = f"@{result[0][1]}, {response[0]}"

                    # 删除特殊符号，防止发送错误
                    response_sent = remove_non_bmp_characters(response_sent)
                    # print(f"删除特殊符号的回复 : {response}")

                    wrapper = SeleniumWrapper("DOUYIN", headless=False)
                    wrapper.send_message(response_sent)  # 发送到抖音

                    # 用于判断是否发送信息到抖音-这里是已发送
                    is_message_sent = True

                else:
                    # 用于判断是否发送信息到抖音-这里是未发送
                    is_message_sent = False

                # 更新表中的数据
                table_name = "scores"
                set_columns = {"answer_content": response[0], "message_sent": is_message_sent}
                conditions = {"id": result[0][0]}
                # 调用 update 方法
                db.update(table_name, set_columns, conditions)

            except Exception as e:
                print(f"An error occurred: {e}")

        else:
            print("No records found with answer_content as NULL.")
            time.sleep(1)

        # 关闭数据库连接
        # db.close_connection()
