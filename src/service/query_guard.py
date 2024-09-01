'''
Author: 杨仕明 shiming.y@qq.com
Date: 2024-08-30 20:36:59
LastEditors: 杨仕明 shiming.y@qq.com
LastEditTime: 2024-08-31 02:09:39
FilePath: /Tik-Tok-Web-fully-automatic-reply/src/service/query_guard.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

import re


def query_guard_own(sentence):
    # 检查输入是否为空值
    if not sentence or not sentence.strip():
        return None

    # 常见的中文疑问词集合
    chinese_question_words = {"吗", "么", "什么", "怎么", "为什么", "是否", "哪", "几", "多少", "多大", "谁", "啥", "哪儿",
                              "能否", "哪里", "哪个", "何时", "怎样", "咋样", "有何", "有么", "对吧", "好吗", "如何", "为啥",
                              "难道", "有没有"}

    # 常见英文疑问词集合
    english_question_words = {"what", "how", "why", "is", "are", "does", "do", "did", "can", "could", "will",
                              "would", "shall", "should", "who", "where", "when", "which", "whom"}

    # 常见的中英文问句短语
    question_phrases = ["你觉得呢", "应该可以吧", "你认为呢", "行不行", "是不是", "可以吗", "能不能", "好不好",
                        "会不会", "这样行吗", "可以不", "对不对", "难道不", "该如何", "怎么办", "这样不好吧",
                        "可不可以",
                        "你觉得", "你怎么看", "行了吧", "aren't you", "isn't it", "could it be", "how about"]

    # 过滤侮辱性或无意义的短语
    non_question_phrases = ["你妈的", "去死", "傻逼", "你丫的", "他妈的", "草你妈", "日你妈", "傻b", "智障",
                            "混蛋", "混账", "滚蛋", "fuck", "shit", "idiot"]

    # 转换为小写字母进行检查（英文部分）
    lower_sentence = sentence.lower()

    # 检查是否包含侮辱性或无意义的短语
    if any(phrase in lower_sentence for phrase in non_question_phrases):
        return False

    # 检查是否包含常见的问句短语
    if any(phrase in lower_sentence for phrase in question_phrases):
        return True

    # 检查是否以数字或纯标点符号作为主要内容的问句
    if re.fullmatch(r'\d+[?？]', sentence) or re.fullmatch(r'[?？]+', sentence):
        return False

    # 检查中文问句
    chinese_pattern = re.compile(rf"(?:({'|'.join(map(re.escape, chinese_question_words))})|(?:.*[啊呢吗呀]?[?？]))")
    if chinese_pattern.search(sentence):
        return True

    # 针对含有方向、比较等关键词的句子进行特殊处理
    direction_words = {"方向", "趋势", "前景", "可能", "选择", "如何", "更好", "更优"}
    if any(word in sentence for word in direction_words) and re.search(r'那些|哪个|哪种', sentence):
        return True

    # 检查隐含疑问语气
    hidden_question_patterns = [r".*了没有$", r".*了没$", r".*吗$", r"有没有.*", r".*咋.*", r".*行不.*"]
    if any(re.search(pattern, sentence) for pattern in hidden_question_patterns):
        return True

    # 专门处理'是吧'、'不是'等情况
    if sentence.endswith("是吧") or sentence.endswith("吧") or sentence.endswith("不是"):
        return True

    # 更准确的问号结尾检查
    trimmed_sentence = sentence.strip()
    if trimmed_sentence.endswith("？") or trimmed_sentence.endswith("?"):
        return True

    # 额外处理问号前后的问句结构
    preceding_text = trimmed_sentence[:-1].strip()
    if re.search(r'\b(吗|是不是|能吗|对吧|好吗|如何|怎么办|行不行|对不对|怎么|为何|为什么|有何|是否|难道)\b', preceding_text):
        return True

    # 检查英文问句
    english_pattern = re.compile(rf"\b({'|'.join(map(re.escape, english_question_words))})\b.*[?]*$")
    if english_pattern.search(lower_sentence):
        return True

    return False

# # 用户输入循环
# while True:
#     user_input = input("请输入句子（输入“退出”以结束）：")
#     if user_input.lower() == "退出":
#         print("程序结束。")
#         break
#     result = query_guard_own(user_input)
#     print(f"检测结果：{result}")

