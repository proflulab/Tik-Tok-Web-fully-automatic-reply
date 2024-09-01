'''
Author: 杨仕明 shiming.y@qq.com
Date: 2024-08-22 21:21:57
LastEditors: 杨仕明 shiming.y@qq.com
LastEditTime: 2024-09-01 09:20:05
FilePath: /Tik-Tok-Web-fully-automatic-reply/src/controller/browser/selenium_driver.py
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

    def __init__(self, headless=False):
        options = Options()
        if headless:
            options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(options=options)
        # self.wait = WebDriverWait(self.driver, 10)

        self.driver.get(DOUYIN_URL)

        if os.path.exists(path_cookie):
            with open(path_cookie, 'rb') as file:
                cookies_list = pickle.load(file)

            for cookie in cookies_list:
                self.driver.add_cookie(cookie)

        else:
            # 等待一段时间，以便手动登录
            time.sleep(1)
            input("登入抖音账号后，请输入任意键继续...")
            time.sleep(0.3)

            # 保存Cookie到文件
            with open(path_cookie, 'wb') as file:
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

    def send_message_element(self, message, xpath):  # 向抖音直播间发送信息

        """发送指定的消息并按下 Enter 键"""
        try:
            # 等待文本区域元素加载并找到
            text_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
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
