'''
Author: 杨仕明 shiming.y@qq.com
Date: 2024-08-22 23:23:43
LastEditors: 杨仕明 shiming.y@qq.com
LastEditTime: 2024-08-22 23:38:58
FilePath: /Tik-Tok-Web-fully-automatic-reply/src/db/sqlite3.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

import sqlite3

# 创建与数据库的连接
conn = sqlite3.connect('test.db')

# conn = sqlite3.connect(':memory:')

# 创建一个游标 cursor
cur = conn.cursor()

# 建表的sql语句
sql_text_1 = '''CREATE TABLE scores
           (姓名 TEXT,
            班级 TEXT,
            性别 TEXT,
            语文 NUMBER,
            数学 NUMBER,
            英语 NUMBER);'''
# 执行sql语句
cur.execute(sql_text_1)

# 插入单条数据
sql_text_2 = "INSERT INTO scores VALUES('A', '一班', '男', 96, 94, 98)"
cur.execute(sql_text_2)

