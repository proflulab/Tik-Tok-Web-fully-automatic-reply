'''
Author: 杨仕明 shiming.y@qq.com and 宋明轩 songmingxuan936@gmail.com
Date: 2024-08-24 09:14:32
LastEditors: 宋明轩 songmingxuan936@gmail.com
LastEditTime: 2024-09-14 08:47:58
FilePath: /Tik-Tok-Web-fully-automatic-reply/src/controller/douyin/get_comments.py
Description:

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved.
'''

import requests
import json
import time
import os

from dotenv import load_dotenv
load_dotenv()

COZE_BOT_ID = os.getenv('COZE_BOT_ID') or'7368796970410459174'
COZE_AUTH = os.getenv('COZE_AUTH') or'*****'


class CozeChatService:

    def __init__(self, bot_id, user_id, api_token):
        self.bot_id = bot_id
        self.user_id = user_id
        self.api_token = api_token
        self.base_url = "https://api.coze.cn/v3/chat"
        self.headers = {
            'Authorization': f'Bearer {self.api_token}',
            'Content-Type': 'application/json'
        }

    def send_message(self, message, stream=False, auto_save_history=True):
        url = self.base_url
        payload = json.dumps({
            "bot_id": self.bot_id,
            "user_id": self.user_id,
            "stream": stream,
            "auto_save_history": auto_save_history,
            "additional_messages": [
                {
                    "role": "user",
                    "content": message,
                    "content_type": "text"
                }
            ]
        })

        response = requests.post(url, headers=self.headers, data=payload)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_retrieve(self, conversation_id, chat_id):
        url = f"{self.base_url}/retrieve?conversation_id={conversation_id}&chat_id={chat_id}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_message_list(self, conversation_id, chat_id):
        url = f"{self.base_url}/message/list?conversation_id={conversation_id}&chat_id={chat_id}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def send_and_get_reply(self, message):
        # Step 1: Send a message and get the chat and conversation IDs
        send_response = self.send_message(message)
        if send_response['code'] != 0:
            raise Exception(f"Error sending message: {send_response['msg']}")

        chat_id = send_response['data']['id']
        conversation_id = send_response['data']['conversation_id']

        while True:
            message_status = self.get_retrieve(conversation_id, chat_id)
            if message_status['code'] != 0:
                raise Exception(f"Error sending message: {message_status['msg']}")

            status = message_status['data']['status']

            if status == "completed":
                break
            else:
                time.sleep(0.2)

        message_list_response = self.get_message_list(conversation_id, chat_id)

        if message_list_response['code'] == 0 and 'data' in message_list_response and message_list_response['data']:
            answer_content = [item['content'] for item in message_list_response['data'] if item['type'] == "answer"]
            return answer_content  # Return once data is present

        raise TimeoutError("Failed to get a complete response from the message list.")


# Example usage
if __name__ == "__main__":
    bot_id = COZE_BOT_ID
    user_id = "123456789"
    api_token = COZE_AUTH

    coze_service = CozeChatService(bot_id, user_id, api_token)

    # Send a message and get the reply
    try:
        response = coze_service.send_and_get_reply("2024年10月1日是星期几")
        print("Full Conversation Response:")
        print(response)
    except Exception as e:
        print(f"An error occurred: {e}")
