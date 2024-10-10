<p align="center">
  <img src="https://github.com/user-attachments/assets/7e57eace-af77-47fd-ba7e-594221e05e1e" alt="97f5c0cd-c7ae-414d-903e-e46fff90adf0_cx0_cy7_cw0_w1200_r1">
</p>

<h1 align="center">抖音网页全自动回复</h1>

<h3 align="center">用户可以使用Python代码实现全自动化，登录、抓取、发送信息、机器人回复

<p align="center">
  <a href="https://github.com/proflulab/Tik-Tok-Web-fully-automatic-reply">
    <img src="https://img.shields.io/github/workflow/status/r-spacex/SpaceX-API/Test?style=flat-square" alt="GitHub Workflow Status">
  </a>
  <a href="https://github.com/Luckymingxuan">
    <img src="https://img.shields.io/badge/作者-Mingxuan-blue" alt="作者-Mingxuan">
  </a>
</p>

<br><br><br><br>

<div align="center" style="font-size: 32px; font-weight: bold; margin: 0; padding: 0;">
    ——= &nbsp;&nbsp;概述&nbsp;&nbsp; =——
</div>

<br><br>

<div align="center" style="text-indent: 20px; margin: 0; padding: 0; font-size: 24px; font-weight: bold;">
    准备工作&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    使用教程&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    待开发项
</div>

<br><br>

<hr><br><br><br>

<h1 align="center">！！！&nbsp;&nbsp;注意 &nbsp;&nbsp;！！！

<h3 align="center">项目暂时仅支持Chrome浏览器
<h3 align="center">需自行在项目目录下创建.env文件( 这部分可以跳转到使用教程 )

<br><br>

<hr>

<br><br><hr><br><br>

<h1 align="center">准备工作

<br><br>

<h3 align="center">——= &nbsp;&nbsp; 设置CozeBot &nbsp;&nbsp; =——

<br><br>

## 获取CozeAPI_TOKEN

现在开始获取coze``api``,找到主页点击左下角``CozeAPI``

<br>

<img src="https://github.com/user-attachments/assets/33c8fd06-fa1a-4941-8bfe-94057ff056e2" alt="image" style="width: 600px; height: auto;">

<br>

创建``API``，请确保``只有你自己知道``，注意保存，这个``只能复制一次``

<img src="https://github.com/user-attachments/assets/37ec8de2-ad83-46bd-a11b-f2d4573fd6a3" alt="image" style="width: 600px; height: auto;">

<br><br>

## 设置CozeBot

<br>

现在要编辑``客服机器人``，找到你刚刚创建的``机器人``，设置为``Agent （工作流模式）``,并且添加你创建的``工作流``

<img src="https://github.com/user-attachments/assets/2f767492-992b-49f2-9f64-090c1ed1d65b" alt="image" style="width: 600px; height: auto;">

<br><br>

## 获取CozeBotId

<br>

找到你``客服机器人上方``的``网址URL``，只需要/bot/后面的``数字部分``

<img src="https://github.com/user-attachments/assets/5546f3b3-b3a5-4b70-99ec-d6f38058cf5d" alt="image" style="width: 600px; height: auto;">

<br><br>

## 发布客服机器人

点击右上角的``发布按钮``，在``选择发布平台下方``勾选``Bot as API``和``Web SDK``

<img src="https://github.com/user-attachments/assets/71d74632-1b66-4dfc-a220-d414e6b5f0f3" alt="image" style="width: 600px; height: auto;">

<br><br>


<h3 align="center">——= &nbsp;&nbsp; 安装Python依赖 &nbsp;&nbsp; =——

<br><br>

## 安装Python库

<br>

使用 pip 来安装``requirements.txt``中列出的所有依赖

```
pip install -r requirements.txt
```

<br>

粘贴在``PyCharm``的``Terminal``里面

<img src="https://github.com/user-attachments/assets/e9f05a0c-f993-484c-a363-434dd050fa35" alt="image" style="width: 600px; height: auto;">

<br><br>

## 安装PyCharm和Chrome到path环境

**注意---如果代码运行能够打开浏览器可以忽略这部操作**

<br>

桌面右键``PyCharm快捷方式``，选择``属性``，获取安装路径

<img src="https://github.com/user-attachments/assets/3f36b4f5-ac49-459f-8807-b53f6105fd9e" alt="image" style="width: 600px; height: auto;">

<br><br>

右键``此电脑``，选择``属性``，点击``高级系统设置``，选择``高级``，选择``环境变量``

<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/user-attachments/assets/85fe830d-a8a5-4d19-aef2-221552b7f89f" alt="Image 1" style="width: 45%; height: auto;">
  <img src="https://github.com/user-attachments/assets/448fadbe-1667-4fd0-bdbc-e06b5e8f0d34" alt="Image 2" style="width: 45%; height: auto;">
</div>

<br><br>

找到上方的``XXX的用户变量``，找到``Path``并``双击``它。点击新建，将复制的安装路径（除去exe文件）粘贴上去

<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/user-attachments/assets/99dbc566-4d1b-4ac9-906d-d7383277d09a" alt="Image 1" style="width: 45%; height: auto;">
  <img src="https://github.com/user-attachments/assets/711a90c9-148f-4279-b575-4d49d0782f3e" alt="Image 2" style="width: 45%; height: auto;">
</div>

<br><br>

安装``Chrome``在``Path``的位置相同，``Path``用于使计算机调用此软件

<br><br>

<hr>

<br><br><hr><br><br>

<h1 align="center">使用教程

<br><br>

<h3 align="center">——= &nbsp;&nbsp; 获取抖音直播间 &nbsp;&nbsp; =——

<br><br>

## 获取抖音直播间号

<br>

找到浏览器``顶部``的``直播间号``

<img src="https://github.com/user-attachments/assets/cb17a848-638c-42c3-9b9d-0fb7a7b77c5a" alt="image" style="width: 600px; height: auto;">

<br><br>

<h3 align="center">——= &nbsp;&nbsp; 配置python文件 &nbsp;&nbsp; =——

<br><br>

## 创建Python配置文件

<br>

这是代码的整体框架

找到``.env.example``文件，复制它，并创建一个``.env``文件

<img src="https://github.com/user-attachments/assets/ec4add60-3d6e-4a05-a75c-fea11148d64c" alt="image" style="width: 600px; height: auto;">

<br><br>

### 这里是``.env``文件

文件结构

```
# 在 .env 文件中定义的环境变量
DOUYIN_LIVE_URL=https://live.douyin.com/
DOUYIN_ROOM=741682777632

#coze机器人的设置
COZE_BOT_ID=7396
COZE_AUTH=pat_8RRGf

#设置是否发送回复到抖音-True是发送-False是不发送
SEND_MESSAGE=False
```

<br><br>


更改``DOUYIN_ROOM``为你自己获取的``直播间号``

```
DOUYIN_ROOM=741682777632
```
<br><br>

更改``COZE_BOT_ID``为你自己获取的``BotId``

更改``COZE_AUTH``为你自己获取的``APITOKEN``

```
#coze机器人的设置
COZE_BOT_ID=7396
COZE_AUTH=pat_8RRGf
```

<br><br>

这里的``SEND_MESSAGE``是用于设置是否发送回复信息到抖音的

这里建议是通常调试的时候默认``False``防止扰乱直播间

```
#设置是否发送回复到抖音-True是发送-False是不发送
SEND_MESSAGE=False
```

<br><br>

<h3 align="center">——= &nbsp;&nbsp; 数据库及登录凭证文件讲解 &nbsp;&nbsp; =——

<br><br>

## 抖音cookie文件
首先运行代码，你如果是第一次登录，程序会``自动弹出`` ``登录页面``并且在输出框提示你``登录后输入任意按键``

这时请你扫码并登录，系统会将文件``自动存储``到``other``文件夹里面

<img src="https://github.com/user-attachments/assets/86740ef4-4036-45a9-9d09-ea6e8af56be9" alt="image" style="width: 600px; height: auto;">

## 数据库相关介绍

上面的图片有指明数据库的位置

在``public``的``db_data``里面

<br>

这个是数据库的结构

<img src="https://github.com/user-attachments/assets/ab97b634-f991-4029-8d08-3489f2e85a21" alt="image" style="width: 600px; height: auto;">

<br>

结构元素分别是

``id`` ``username`` ``question_time`` ``comment_content`` ``question_judgment`` ``message_sent`` ``answer_content``

<br><br>

### 数据库整体架构



<div align="center">

| id      | username | question_time    | comment_content | question_judgment | message_sent | message_sent       |
|---------|----------|------------------|-----------------|-------------------|--------------|--------------------|
| 用户id | 用户名称 | 发送评论的时间 | 评论内容 | 问句判断 | 发送信息的状态 | 客服机器人回复 |
| cadde4fa-abc3-40a4-88ac-1234 | 用*** | 1726821999.56544 | 有没有课程啊 | 1  | 1 | 您好！相关课程.... |

</div>

<br>

发送到抖音的内容
```
@用***, 您好！相关课程....
```

<br><br>

<hr>

<br><br><hr><br><br>

<h1 align="center">待开发项

<br><br>

## 实现功能

- [x] 自动获取直播间信息
- [x] 自动发送信息
- [x] 三线程提高效率
- [x] 算法判断问句
- [ ] 数据实时同步至多维表
- [ ] 更好的微调模型


## 待开发

- 对接多维表，数据实时同步至多维表（尹航, 9月25日）
- 优化问题
  - 优化加载速度
  - 增加调试功能
  - 优化客服的回复准确性
  - 尝试可视化页面
- 对接多维表，数据实时同步至多维表（尹航, 9月25日）
- 数据集收集
  - 收集并整理数据到飞书（尹航, 9月25日）
- 增加敏感词过滤模块
- 验证模块主动识别

## 参考资料

教程：使用Python和Selenium自动化抖音互动
https://dashen.wang/6174.html
