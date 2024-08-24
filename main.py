'''
Author: 杨仕明 shiming.y@qq.com
Date: 2024-08-22 21:19:26
LastEditors: 杨仕明 shiming.y@qq.com
LastEditTime: 2024-08-22 22:49:23
FilePath: /Tik-Tok-Web-fully-automatic-reply/main.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

from selenium import webdriver
from dotenv import load_dotenv
import time
import pickle

from src.browser.douyin_login import login_and_save_cookies

import os

load_dotenv()
TIKTOK_URL = os.getenv('TIKTOK_URL') or 'https://live.douyin.com/'
TIKTOK_ROOM = os.getenv('TIKTOK_ROOM') or '53417358783'

if __name__ == '__main__':

    while (True):
        print("434")
        # Check if the cookie file exists
        if os.path.exists("douyin_cookie.pickle"):
            # Load the previously saved cookies
            with open("douyin_cookie.pickle", 'rb') as file:
                cookies_list = pickle.load(file)

            # Create a Chrome browser instance
            chrome = webdriver.Chrome()

            # Open the Douyin website
            chrome.get(TIKTOK_URL)

            # Add cookies to maintain login state
            for cookie in cookies_list:
                chrome.add_cookie(cookie)

            # Enter the specific live room link
            chrome.get(TIKTOK_URL + TIKTOK_ROOM)  # Example: New Oriental live room

            # Wait for some time to ensure the page loads completely
            time.sleep(10)
            break
        else:
            # If the cookie file does not exist, run the login function
            login_and_save_cookies()

# def main():  # 启动多线程
#     # 启动线程
#     thread1 = threading.Thread(target=monitor_screen, name="MonitorScreen")
#     thread2 = threading.Thread(target=run_main_thread_question_judgment, name="QuestionJudgmentThread")
#     thread3 = threading.Thread(target=run_main_thread_reply, name="BotReplyThread")

#     global data_list  # 用于处理用户回复
#     data_list = []  # 清空数据列表

#     thread1.start()  # 这个线程用于获取抖音直播用户的评论
#     thread2.start()  # 这个用于判断问句并在输出框发送句型，用户名，评论
#     thread3.start()  # 这个线程用于回复那些是问句的问题

