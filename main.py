'''
Author: 杨仕明 shiming.y@qq.com
Date: 2024-08-22 21:19:26
LastEditors: 杨仕明 shiming.y@qq.com
LastEditTime: 2024-08-30 20:12:18
FilePath: /Tik-Tok-Web-fully-automatic-reply/main.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

# from dotenv import load_dotenv
import threading

# from src.controller.douyin.login import login_and_save_cookies
from src.controller.douyin.get_comments import get_comments
from src.controller.browser.selenium_driver import SeleniumWrapper
from src.service.db.sqlite import SQLiteHelper

# load_dotenv()
# DOUYIN_URL = os.getenv('DOUYIN_URL') or'https://www.douyin.com/'
# DOUYIN_LIVE_URL = os.getenv('DOUYIN_LIVE_URL') or'https://www.douyin.com/'
# DOUYIN_ROOM = os.getenv('DOUYIN_ROOM') or '53417358783'

# path_cookie = os.path.join(os.getcwd(), "src/public/other/douyin_cookie.pickle")

# init
wrapper = SeleniumWrapper(headless=False)
db = SQLiteHelper("src/public/db_data/data.db")
db.create_connection()

if __name__ == '__main__':

    sql_text = "CREATE TABLE scores (编号 TEXT,用户名 TEXT,提问时间 TEXT,问题 TEXT,回答 TEXT);"
    db.execute_query(sql_text)

    thread1 = threading.Thread(target=get_comments, name="MonitorScreen")
    # thread2 = threading.Thread(target=run_main_thread_question_judgment, name="QuestionJudgmentThread")
    # thread3 = threading.Thread(target=run_main_thread_reply, name="BotReplyThread")

    thread1.start()  # 这个线程用于获取抖音直播用户的评论
    # thread2.start()  # 这个用于判断问句并在输出框发送句型，用户名，评论
    # thread3.start()  # 这个线程用于回复那些是问句的问题
