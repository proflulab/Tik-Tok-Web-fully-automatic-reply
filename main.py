'''
Author: 杨仕明 shiming.y@qq.com
Date: 2024-08-22 21:19:26
LastEditors: 杨仕明 shiming.y@qq.com
LastEditTime: 2024-08-29 21:22:15
FilePath: /Tik-Tok-Web-fully-automatic-reply/main.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

# from dotenv import load_dotenv
# import threading
# import pickle

# from src.controller.douyin.login import login_and_save_cookies
# from src.controller.douyin.get_comments import get_comments
from src.controller.browser.selenium_driver import SeleniumWrapper

import os

# load_dotenv()
# DOUYIN_URL = os.getenv('DOUYIN_URL') or'https://www.douyin.com/'
# DOUYIN_LIVE_URL = os.getenv('DOUYIN_LIVE_URL') or'https://www.douyin.com/'
# DOUYIN_ROOM = os.getenv('DOUYIN_ROOM') or '53417358783'

path_cookie = os.path.join(os.getcwd(), "src/public/other/douyin_cookie.pickle")

if __name__ == '__main__':

    wrapper = SeleniumWrapper(headless=False)
    
    # wrapper.__init__()

    # while (True):
    #     wrapper = SeleniumWrapper(headless=False)

    #     # Check if the cookie file exists
    #     if os.path.exists(path_cookie):
    #         # Load the previously saved cookies
    #         with open(path_cookie, 'rb') as file:
    #             cookies_list = pickle.load(file)

    #         # wrapper.open_url(DOUYIN_URL)

    #         # # Create a Chrome browser instance
    #         # chrome = webdriver.Chrome()

    #         # # Open the Douyin website
    #         # chrome.get(DOUYIN_URL)

    #         # # Add cookies to maintain login state
    #         # for cookie in cookies_list:
    #         #     chrome.add_cookie(cookie)

    #         # # Enter the specific live room link
    #         # chrome.get(DOUYIN_LIVE_URL + DOUYIN_ROOM)  # Example: New Oriental live room

    #         input("加载cookie后预留时间操作其他认证，请输入任意键继续...")
    #         break
    #     else:
    #         # If the cookie file does not exist, run the login function
    #         login_and_save_cookies()

    # 判断数据库是否存在，如何不存在，则创建一个数据库

    # thread1 = threading.Thread(target=get_comments, name="MonitorScreen")
    # thread2 = threading.Thread(target=run_main_thread_question_judgment, name="QuestionJudgmentThread")
    # thread3 = threading.Thread(target=run_main_thread_reply, name="BotReplyThread")

    # thread1.start()  # 这个线程用于获取抖音直播用户的评论
    # thread2.start()  # 这个用于判断问句并在输出框发送句型，用户名，评论
    # thread3.start()  # 这个线程用于回复那些是问句的问题
