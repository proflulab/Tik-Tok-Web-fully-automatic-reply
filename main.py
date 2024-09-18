'''
Author: 杨仕明 shiming.y@qq.com, 宋明轩 songmingxuan936@gmail.com
Date: 2024-08-24 09:14:32
LastEditors: 宋明轩 songmingxuan936@gmail.com
LastEditTime: 2024-09-16 20:30:54
FilePath: /Tik-Tok-Web-fully-automatic-reply/src/controller/douyin/get_comments.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

import threading

from src.controller.douyin.get_comments import get_comments
from src.controller.douyin.ask_guard import ask_guard
from src.service.db.sqlite import SQLiteHelper
from src.controller.douyin.ai_response import ai_response

# init
db = SQLiteHelper("src/public/db_data/data.db")
db.create_connection()

if __name__ == '__main__':

    sql_text = "CREATE TABLE scores (id TEXT,username TEXT,question_time TEXT,comment_content TEXT,question_judgment BOOLEAN,message_sent BOOLEAN,answer_content TEXT);"
    db.execute_query(sql_text)

    thread1 = threading.Thread(target=get_comments, name="MonitorScreen")
    thread2 = threading.Thread(target=ask_guard, name="ask_guard")
    thread3 = threading.Thread(target=ai_response, name="BotReplyThread")

    thread1.start()  # 这个线程用于获取抖音直播用户的评论
    thread2.start()  # 这个用于判断问句并在输出框发送句型，用户名，评论
    thread3.start()  # 这个线程用于回复那些是问句的问题
