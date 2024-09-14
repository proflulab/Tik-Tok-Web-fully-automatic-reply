'''
Author: 杨仕明 shiming.y@qq.com and 宋明轩 songmingxuan936@gmail.com
Date: 2024-08-24 09:14:32
LastEditors: 宋明轩 songmingxuan936@gmail.com
LastEditTime: 2024-09-14 08:47:58
FilePath: /Tik-Tok-Web-fully-automatic-reply/src/controller/douyin/get_comments.py
Description:

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved.
'''

from src.service.query_guard import query_guard_own
import time


def ask_guard():  # 获取用户在抖音直播间发送的信息

    while True:
        # 查询 question_time 最小且 question_judgment 为空的一条数据
        query = """
        SELECT *
        FROM scores
        WHERE question_judgment IS NULL OR question_judgment = ''
        ORDER BY question_time ASC
        LIMIT 1;
        """

        from main import db

        result = db.fetch_all(query)

        if result:
            print("The record with the minimum question_time and a NULL question_judgment is:")
            print(result)

            if query_guard_own(result[0][3]):

                # 更新表中的数据
                table_name = "scores"
                set_columns = {"question_judgment": True}
                conditions = {"id": result[0][0]}
                # 调用 update 方法
                db.update(table_name, set_columns, conditions)

            else:
                # 更新表中的数据
                table_name = "scores"
                set_columns = {"question_judgment": False}
                conditions = {"id": result[0][0]}
                # 调用 update 方法
                db.update(table_name, set_columns, conditions)

        else:
            print("No records found with question_judgment as NULL.")
            time.sleep(1)

        # 关闭数据库连接
        # db.close_connection()
