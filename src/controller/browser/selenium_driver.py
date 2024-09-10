'''
Author: 杨仕明 shiming.y@qq.com
Date: 2024-08-22 21:21:57
LastEditors: 杨仕明 shiming.y@qq.com
LastEditTime: 2024-09-01 02:19:19
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
    _instance = None  # 防止浏览器重复打开

    def __new__(cls, headless=False):
        if cls._instance is None:  # 如果实例还不存在，则创建实例
            cls._instance = super(SeleniumWrapper, cls).__new__(cls)
            options = Options()
            if headless:
                options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')

            cls._instance.driver = webdriver.Chrome(options=options)
            # self.wait = WebDriverWait(self.driver, 10)

            cls._instance.driver.get(DOUYIN_URL)

            if os.path.exists(path_cookie):
                with open(path_cookie, 'rb') as file:
                    cookies_list = pickle.load(file)

                for cookie in cookies_list:
                    cls._instance.driver.add_cookie(cookie)

            else:
                # 等待一段时间，以便手动登录
                time.sleep(1)
                input("登入抖音账号后，请输入任意键继续...")
                time.sleep(0.3)

                # 保存Cookie到文件
                with open(path_cookie, 'wb') as file:
                    pickle.dump(cls._instance.driver.get_cookies(), file)

        # 返回实例
        return cls._instance

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

# # 示例使用
# if __name__ == "__main__":
#     driver_path = '/path/to/chromedriver'  # 替换为你自己的chromedriver路径
#     wrapper = SeleniumWrapper(driver_path, headless=False)
    
#     wrapper.open_url('https://www.google.com')
#     wrapper.enter_text(By.NAME, 'q', 'Python Selenium')
#     wrapper.click_element(By.NAME, 'btnK')
    
#     time.sleep(5)  # 等待几秒查看结果
#     wrapper.close_browser()
