'''
Author: 杨仕明 shiming.y@qq.com, 宋明轩 songmingxuan936@gmail.com
Date: 2024-08-24 09:14:32
LastEditors: 宋明轩 songmingxuan936@gmail.com
LastEditTime: 2024-09-16 20:30:54
FilePath: /Tik-Tok-Web-fully-automatic-reply/src/controller/douyin/get_comments.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

import os
import pickle
from dotenv import load_dotenv

load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))
path_cookie = os.path.join(current_dir, "../../public/other/douyin_cookie.pickle")

DOUYIN_URL = os.getenv('DOUYIN_URL') or'https://www.douyin.com/'


class SeleniumWrapper:
    web_instances = {}  # 存储不同的 web 实例

    web_name = None  # 类属性，给所有实例一个默认值
    driver = None  # 类属性，给所有实例一个默认值

    def __new__(cls, web_name, headless=False):
        """创建或返回已存在的实例"""
        if web_name in cls.web_instances:
            return cls.web_instances[web_name]  # 如果实例已存在，直接返回

        # 如果实例不存在，创建新的实例
        new_web_instances = super(SeleniumWrapper, cls).__new__(cls)
        cls.web_instances[web_name] = new_web_instances  # 存储实例
        new_web_instances.create_web(web_name, headless)  # 创建 web 实例
        return new_web_instances

    def create_web(self, web_name, headless=False):
        """创建 Web 实例并加载配置"""
        self.web_name = web_name
        options = Options()
        if headless:
            options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(options=options)
        self.driver.get(DOUYIN_URL)

        # 调用加载 Cookie 文件
        if os.path.exists(path_cookie):
            # 加载 Cookie 文件
            self.load_cookies(path_cookie)
        else:
            # 保存 Cookie 文件到本地
            self.save_cookies(path_cookie)

            # 加载 Cookie 文件
            self.load_cookies(path_cookie)

    def load_cookies(self, cookie_path):
        # 加载 Cookie 文件
        with open(cookie_path, 'rb') as file:
            cookies_list = pickle.load(file)

        for cookie in cookies_list:
            self.driver.add_cookie(cookie)

    def save_cookies(self, cookie_path):
        # 保存 Cookie 文件

        # 等待用户手动登录
        time.sleep(1)
        input("登入抖音账号后，请输入任意键继续...")
        time.sleep(0.3)

        # 保存 Cookies 到文件
        with open(cookie_path, 'wb') as file:
            pickle.dump(self.driver.get_cookies(), file)

    def open_url(self, url):
        self.driver.get(url)
        print(f"Opened URL: {url}")

    def find_element(self, by, value):
        element = self.wait.until(EC.presence_of_element_located((by, value)))
        print(f"Found element by {by} with value {value}")
        return element

    def click_element(self, by, value):
        element = self.find_element(by, value)
        element.click()
        print(f"Clicked on element by {by} with value {value}")

    def enter_text(self, by, value, text):
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)
        print(f"Entered text into element by {by} with value {value}: {text}")

    def close_browser(self):
        self.driver.quit()
        print("Closed browser")

    def send_message(self, message):  # 向抖音直播间发送信息
        """发送指定的消息并按下 Enter 键"""
        try:
            # 等待文本区域元素加载并找到
            text_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//textarea[@class="webcast-chatroom___textarea"]'))
            )
            text_element.clear()
            text_element.send_keys(message)
            time.sleep(0.5)

            # 按下 Enter 键发送消息
            text_element.send_keys(Keys.RETURN)
        except Exception as e:
            print(f"发送消息时发生错误: {e}")

# # 示例使用
# if __name__ == "__main__":
#     driver_path = '/path/to/chromedriver'  # 替换为你自己的chromedriver路径
#     wrapper = SeleniumWrapper(driver_path, headless=False)
    
#     wrapper.open_url('https://www.google.com')
#     wrapper.enter_text(By.NAME, 'q', 'Python Selenium')
#     wrapper.click_element(By.NAME, 'btnK')
    
#     time.sleep(5)  # 等待几秒查看结果
#     wrapper.close_browser()
