import random
import time
import os
from dotenv import load_dotenv
from src.service.coze import CozeChatService
from src.controller.browser.selenium_driver import SeleniumWrapper
from src.controller.douyin.get_comments import remove_non_bmp_characters

load_dotenv()

COZE_BOT_ID = os.getenv('COZE_BOT_ID') or '7368796970410459174'
COZE_AUTH = os.getenv('COZE_AUTH') or '*****'

# 如果环境变量SEND_MESSAGE为True，则启用消息发送
Send_Message = os.getenv('SEND_MESSAGE', 'False').lower() == 'true'

WELCOME_MESSAGES = [
    "新进直播间的朋友们，左上角点个关注，不错过陆老师的每场直播",
    "左上角加个粉丝灯牌，下次陆老师讲干货的时候，就会自动推送给您。",
    "请把直播间转发给您需要的亲友，帮他们提供最前沿的教育方法。",
    "大家有问题可以打在评论区跟陆老师互动哈",
    "大家想拍的抓紧了,今天直播间拍有特价,原价8880元,直播间优惠2000元",
    "寒假AI训练营开售啦! 12月份批次的12月14日开始,1月份批次的1月18日开始,四周24次课",
    "今天陆老师专场和您畅聊如何培养少年英才，您可以发上来您对孩子教育的思考，或者孩子的具体情况",
]

def ai_response():  # 获取用户在抖音直播间发送的信息
    last_welcome_time = time.time()  # 初始化上次发送欢迎消息的时间

    while True:
        # 查询 question_time 最小且 question_judgment 为 1，answer_content 为空，auto_block 为 0 的一条数据
        query = """
        SELECT *
        FROM scores
        WHERE question_judgment = 1
          AND (answer_content IS NULL OR answer_content = '')
          AND auto_block = 0
        ORDER BY question_time ASC
        LIMIT 1;
        """
        from main import db
        result = db.fetch_all(query)

        # 检查是否到了发送欢迎消息的时间
        current_time = time.time()
        if current_time - last_welcome_time >= random.randint(240, 360):  # 每4到6分钟发送一次
            send_welcome_message()  # 调用发送欢迎消息的函数
            last_welcome_time = current_time  # 更新上次发送欢迎消息的时间

        # 处理数据库中未回复的消息
        if result:
            print("The record with the minimum question_time and a NULL question_judgment is:")
            print(result)

            bot_id = COZE_BOT_ID
            user_id = "12345678978976"
            api_token = COZE_AUTH

            coze_service = CozeChatService(bot_id, user_id, api_token)

            # 发送用户问题并获取回复
            try:
                response = coze_service.send_and_get_reply(result[0][3])
                print("Full Conversation Response:")

                # 拼接回复格式并发送到抖音
                if Send_Message:
                    response_sent = f"@{result[0][1]}, {response[0]}"
                    response_sent = remove_non_bmp_characters(response_sent)

                    wrapper = SeleniumWrapper("DOUYIN", headless=False)
                    wrapper.send_message(response_sent)
                    is_message_sent = True
                else:
                    is_message_sent = False

                # 更新数据库记录
                table_name = "scores"
                set_columns = {"answer_content": response[0], "message_sent": is_message_sent}
                conditions = {"id": result[0][0]}
                db.update(table_name, set_columns, conditions)

            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("No records found with answer_content as NULL.")
            time.sleep(1)

def send_welcome_message():
    # 随机选择一条欢迎消息
    welcome_message = random.choice(WELCOME_MESSAGES)
    
    # 发送欢迎消息到直播间
    if Send_Message:
        wrapper = SeleniumWrapper("DOUYIN", headless=False)
        try:
            wrapper.send_message(welcome_message)
            print(f"欢迎消息已发送：{welcome_message}")
        except Exception as e:
            print(f"发送欢迎消息时发生错误: {e}")
    else:
        print("Send_Message 环境变量为 False, 未发送欢迎消息")
