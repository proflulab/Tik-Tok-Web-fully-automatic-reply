import re


def profanity_block(sentence):
    # 检查输入是否为空值
    if not sentence or not sentence.strip():
        return None

    # 过滤侮辱性或无意义的短语
    profanity_phrases = ["你妈的", "去死", "傻逼", "你丫的", "他妈的", "草你妈", "日你妈", "傻b", "智障", "cnm",
                         "废物", "去你妈的", "你他妈的", "cnmd", "去他妈的", "去踏马的", "垃圾", "丑b", "你丫的",
                         "混蛋", "混账", "滚蛋", "fuck", "shit", "idiot", "踏马的", "你踏马"]

    # 过滤侮辱性或无意义的短语
    irony_phrases = ["骗子太多明显傻子不够用了", "你个骗子", "花钱听废话真划算", "这个课不买就赚了", "又是一堂充满套路的课",
                     "花钱学习怎么被忽悠", "买课就是成功的开始？", "要是学这个能发财，老师还在这教课", "上课不用心，收钱倒是真快",
                     "这课都敢收费？真有你的","这课都敢收费", "老师懂AI算法吗？不就是在背PPT？", "AI课都能这么卖了？知识真是个好生意！",
                     "这课多学几次，能让我成马斯克吗？", "你怕不是在割韭菜", "课学完，我是不是就要起飞了", "课买了，啥时候才能回本啊",
                     "又是一个‘包会AI’的神奇课程"]

    # 转换为小写字母进行检查（英文部分）
    lower_sentence = sentence.lower()

    # 检查是否包含侮辱性短语
    if any(phrase in lower_sentence for phrase in profanity_phrases):
        return True

    # 检查“去...死”模式，允许任意字符（包括汉字、空格等）
    if re.search(r'去.+?死', lower_sentence):
        return True

    # 检查是否包含讽刺短语
    if any(phrase in lower_sentence for phrase in irony_phrases):
        return True

    # 检查是否包含“陆老师”或“陆向谦”或“清华教授”并且包含“骗子”
    if (re.search(r'(陆|向谦|教授|清华).*骗子', sentence) or
        re.search(r'骗子.*(陆|向谦|教授|清华)', sentence)):
        return True

    # 检查是否包含“陆老师”或“陆向谦”或“清华教授”，并且包含“没有”或“不是”，并包含“教授”、“清华”或“老师”
    if (re.search(r'(陆|向谦|教授|清华)', sentence) and
        re.search(r'(没有|不是|不配)', sentence) and
        re.search(r'(教授|清华|老师)', sentence)):
        return True

    # 检查是否包含“这个课”，“陆老师”并包含“没用”、“垃圾”或“骗人”
    if re.search(r'(这个课|课程|陆|向谦|教授|清华)', sentence) and re.search(r'(没用|垃圾|骗人)', sentence):
        return True

    return False


if profanity_block("去踏马死吧"):
    print("True")
else:
    print("False")


print(profanity_block)
