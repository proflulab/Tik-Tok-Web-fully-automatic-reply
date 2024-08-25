'''
Author: 杨仕明 shiming.y@qq.com
Date: 2024-08-22 21:07:29
LastEditors: 杨仕明 shiming.y@qq.com
LastEditTime: 2024-08-22 21:07:42
FilePath: /Tik-Tok-Web-fully-automatic-reply/browser/douyin_login.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
# 文件名：douyin_login.py

from selenium import webdriver
import time
import pickle


def login_and_save_cookies():
    # 创建Edge浏览器实例
    chrome = webdriver.Chrome()

    # 最大化浏览器窗口
    chrome.maximize_window()

    # 设置最大等待时长为10秒
    chrome.implicitly_wait(10)

    # 打开抖音网站
    chrome.get('https://www.douyin.com/')

    # 等待一段时间，以便手动登录
    time.sleep(1)
    input("登入抖音账号后，请输入任意键继续...")
    time.sleep(0.3)

    # 保存Cookie到文件
    with open("douyin_cookie.pickle", 'wb') as file:
        pickle.dump(chrome.get_cookies(), file)

    # 删除浏览器中的所有Cookie
    chrome.delete_all_cookies()

    # 关闭浏览器
    chrome.quit()
