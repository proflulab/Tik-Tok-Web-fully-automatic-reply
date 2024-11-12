# from src.service.db.sqlite import SQLiteHelper
#
# import os
#
# print(os.path.abspath("src/public/db_blacklist/douyin_blacklist.db"))
#
# # db_blacklist = SQLiteHelper("src/public/db_blacklist/douyin_blacklist.db")
# db_blacklist = SQLiteHelper(os.path.join(os.getcwd(), "../public/db_blacklist/blacklist.db"))
#
# db_blacklist.create_connection()
#
# sql_blacklist_text = """
# CREATE TABLE scores (
#     id TEXT,
#     username TEXT,
#     question_time TEXT,
#     comment_content TEXT,
#     auto_block BOOLEAN,
#     douyin BOOLEAN,
#     wechat_channel BOOLEAN
# );
# """
#
# db_blacklist.execute_query(sql_blacklist_text)
#
#
# sql_text = "INSERT INTO scores VALUES(?, ?, ?, ?, ?, ?, ?)"
# db_blacklist.execute_query(sql_text, ("1234", "testtest", "1122323", "helloworld", '这个是demo文件', '', ''))


def check_black(user_name):
    # 查询用户是否在黑名单里面
    query = """
    SELECT *
    FROM scores
    WHERE username = ?
    LIMIT 1;
    """

    from main import db_blacklist

    # 执行查询，将 user_name 作为参数传入
    result = db_blacklist.fetch_all(query, (user_name,))

    # 如果 result 有内容，则说明存在匹配的记录，返回 True，否则返回 False
    return bool(result)


# lest = check_black("nihao")
# print(lest)

