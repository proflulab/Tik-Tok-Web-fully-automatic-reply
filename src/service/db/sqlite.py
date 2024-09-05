'''
Author: 杨仕明 shiming.y@qq.com
Date: 2024-08-22 23:23:43
LastEditors: 杨仕明 shiming.y@qq.com
LastEditTime: 2024-08-30 17:17:18
FilePath: /Tik-Tok-Web-fully-automatic-reply/src/service/db/sqlite.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

import sqlite3
from sqlite3 import Error


class SQLiteHelper:

    def __init__(self, db_file):
        """初始化连接到 SQLite 数据库的实例"""
        self.db_file = db_file
        self.connection = None

    def create_connection(self):
        """创建数据库连接"""
        try:
            self.connection = sqlite3.connect(self.db_file, check_same_thread=False)
            print(f"连接到 SQLite 数据库成功: {self.db_file}")
        except Error as e:
            print(f"连接错误: {e}")

    def table_exists(self, table_name):
        """检查表是否存在"""
        query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';"
        result = self.execute_query(query)
        return len(result) > 0

    def get_table_columns(self, table_name):
        """获取表的字段信息"""
        query = f"PRAGMA table_info({table_name});"
        result = self.execute_query(query)
        return [row[1] for row in result]  # 获取每个字段的名字

    def update_table(self, table_name, required_columns):
        """更新表的字段"""
        current_columns = self.get_table_columns(self, table_name)
        missing_columns = [col for col in required_columns if col not in current_columns]

        if missing_columns:
            for column in missing_columns:
                alter_query = f"ALTER TABLE {table_name} ADD COLUMN {column};"
                self.execute_query(alter_query)
            print(f"更新表 {table_name}，新增字段: {missing_columns}")
        else:
            print(f"表 {table_name} 已包含所有字段，无需更新")

    def close_connection(self):
        """关闭数据库连接"""
        if self.connection:
            self.connection.close()
            print("数据库连接已关闭")

    def execute_query(self, query, params=None):
        """执行 SQL 查询"""
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            print("查询执行成功")
        except Error as e:
            print(f"查询执行错误: {e}")

    def fetch_all(self, query, params=None):
        """执行 SELECT 查询并返回所有结果"""
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"查询错误: {e}")
            return None

    def insert(self, table, columns, values):
        """插入数据到表中"""
        placeholders = ', '.join(['?'] * len(values))
        columns_str = ', '.join(columns)
        query = f"INSERT INTO {table} ({columns_str}) VALUES ({placeholders})"
        self.execute_query(query, values)

    def update(self, table, set_columns, conditions):
        """更新表中的数据"""
        set_str = ', '.join([f"{col} = ?" for col in set_columns.keys()])
        condition_str = ' AND '.join([f"{col} = ?" for col in conditions.keys()])
        query = f"UPDATE {table} SET {set_str} WHERE {condition_str}"
        params = list(set_columns.values()) + list(conditions.values())
        self.execute_query(query, params)

    def delete(self, table, conditions):
        """删除表中的数据"""
        condition_str = ' AND '.join([f"{col} = ?" for col in conditions.keys()])
        query = f"DELETE FROM {table} WHERE {condition_str}"
        params = list(conditions.values())
        self.execute_query(query, params)

# # 使用示例
# if __name__ == "__main__":
#     db = SQLiteHelper("example.db")
#     db.create_connection()

#     # 插入数据
#     db.insert("users", ["name", "age"], ["Alice", 30])

#     # 查询数据
#     results = db.fetch_all("SELECT * FROM users")
#     print(results)

#     # 更新数据
#     db.update("users", {"age": 31}, {"name": "Alice"})

#     # 删除数据
#     db.delete("users", {"name": "Alice"})

#     db.close_connection()


