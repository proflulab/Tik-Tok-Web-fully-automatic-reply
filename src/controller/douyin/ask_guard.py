'''
Author: 杨仕明 shiming.y@qq.com, 宋明轩 songmingxuan936@gmail.com
Date: 2024-08-24 09:14:32
LastEditors: 宋明轩 songmingxuan936@gmail.com
LastEditTime: 2024-09-16 20:30:54
FilePath: /Tik-Tok-Web-fully-automatic-reply/src/controller/douyin/get_comments.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

from src.service.query_guard import query_guard_own
from src.service.profanity_block import profanity_block
import time


def ask_guard():  # 获取用户在抖音直播间发送的信息

    while True:
        # 查询 question_time 最小且 question_judgment 为空的一条数据 和 auto_block 为 0 或空值的一条数据
        query = """
        SELECT *
        FROM scores
        WHERE (question_judgment IS NULL OR question_judgment = '')
          AND (auto_block IS NULL OR auto_block = '' OR auto_block = 0)
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
                conditions = {"id": result[0][0]}

                if profanity_block(result[0][3]):
                    # 判断是否存在侮辱性词语

                    # 将用户信息储存到黑名单里面
                    from main import db_blacklist
                    sql_text = "INSERT INTO scores VALUES(?, ?, ?, ?, ?, ?, ?)"
                    db_blacklist.execute_query(sql_text, (result[0][0], result[0][1], result[0][2], result[0][3], True, "", ""))

                    set_columns = {"question_judgment": True, "auto_block": True}
                    print("已屏蔽这段脏话，并拉入黑名单")
                else:
                    set_columns = {"question_judgment": True, "auto_block": False}

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
