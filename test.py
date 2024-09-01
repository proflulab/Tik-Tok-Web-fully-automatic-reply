'''
Author: 杨仕明 shiming.y@qq.com
Date: 2024-08-22 21:19:26
LastEditors: 杨仕明 shiming.y@qq.com
LastEditTime: 2024-08-31 10:19:44
FilePath: /Tik-Tok-Web-fully-automatic-reply/test.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

import threading

# from src.controller.douyin.get_comments import get_comments
# from src.controller.douyin.ask_guard import ask_guard
# from src.controller.browser.selenium_driver import SeleniumWrapper
from src.service.db.sqlite import SQLiteHelper
from src.controller.douyin.ai_response import ai_response

# init
# wrapper = SeleniumWrapper(headless=False)
db = SQLiteHelper("src/public/db_data/data.db")
db.create_connection()

if __name__ == '__main__':

    # sql_text = "CREATE TABLE scores (id TEXT,username TEXT,question_time TEXT,comment_content TEXT,question_judgment BOOLEAN,answer_content TEXT);"
    # db.execute_query(sql_text)

    # for i in range(10):
    #     sql_text_2 = "INSERT INTO scores VALUES(?, ?, ?, ?, ?,?)"
    #     db.execute_query(sql_text_2, ('1', '2', time.time(), '423567843', '', ''))
    #     time.sleep(1)

    # thread1 = threading.Thread(target=get_comments, name="MonitorScreen")
    # thread2 = threading.Thread(target=ask_guard, name="ask_guard")
    thread3 = threading.Thread(target=ai_response, name="BotReplyThread")

    # thread1.start()  # 这个线程用于获取抖音直播用户的评论
    # thread2.start()  # 这个用于判断问句并在输出框发送句型，用户名，评论
    thread3.start()  # 这个线程用于回复那些是问句的问题
