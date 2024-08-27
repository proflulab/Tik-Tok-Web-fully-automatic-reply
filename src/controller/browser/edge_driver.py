'''
Author: 杨仕明 shiming.y@qq.com
Date: 2024-08-22 21:21:57
LastEditors: 杨仕明 shiming.y@qq.com
LastEditTime: 2024-08-22 22:16:14
FilePath: /Tik-Tok-Web-fully-automatic-reply/browser/edge_driver.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def chrome_driver():  # 打开浏览器
    options = Options()
    options.add_argument("--start-maximized")  # 启动时最大化窗口
    return webdriver.Chrome(options=options)  # 默认使用chromedriver的系统路径
