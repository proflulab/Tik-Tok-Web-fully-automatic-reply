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

<h1 align="center">概述</h1>

<br><br>

<h2 align="center" style="text-indent: 20px; margin: 0; padding: 0;">
    部署教程&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    原理展示&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    常见问题
</h2>

<br><br><br><br>

<h1 align="center">部署教程</h1>

<br>

## 安装python库

<br>

安装用于获取网页端元素位置的库

```
pip install selenium
```

安装存储到Excel里面的库

```
pip install pandas openpyxl
```
<br>

粘贴在**PyCharm**的**Terminal**里面

<img src="https://github.com/user-attachments/assets/e9f05a0c-f993-484c-a363-434dd050fa35" alt="image" style="width: 600px; height: auto;">

<br><br>

## 安装PyCharm和Chrome到path环境

<br>

右键**PyCharm快捷方式**，选择**属性**，获取安装路径

<img src="https://github.com/user-attachments/assets/3f36b4f5-ac49-459f-8807-b53f6105fd9e" alt="image" style="width: 600px; height: auto;">

<br><br>

右键**此电脑**，选择**属性**，点击高级系统设置，选择高级，选择环境变量

<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/user-attachments/assets/85fe830d-a8a5-4d19-aef2-221552b7f89f" alt="Image 1" style="width: 45%; height: auto;">
  <img src="https://github.com/user-attachments/assets/448fadbe-1667-4fd0-bdbc-e06b5e8f0d34" alt="Image 2" style="width: 45%; height: auto;">
</div>

<br><br>

找到上方的**XXX的用户变量**，找到**Path**并**双击**它。点击新建，将复制的安装路径（除去exe文件）粘贴上去

<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/user-attachments/assets/99dbc566-4d1b-4ac9-906d-d7383277d09a" alt="Image 1" style="width: 45%; height: auto;">
  <img src="https://github.com/user-attachments/assets/711a90c9-148f-4279-b575-4d49d0782f3e" alt="Image 2" style="width: 45%; height: auto;">
</div>

<br><br>

安装**Chrome**在**Path**的位置相同，**Path**用于使计算机调用此软件

<br><br>

## 获取抖音登录Cookie

<br>

首先，这需要用到**python**代码，找到GitHub文件中的Automatically_obtain_login.py下载下来，运行一下。
运行后，你需要**扫描登录**你的抖音账户，在输出框输入**任意按键**，就能得到你的**登录Cookie**，**请不要发给任何人**

<img src="https://github.com/user-attachments/assets/d12d031f-2da7-4a40-b0b9-5c87effe995c" alt="image" style="width: 600px; height: auto;">

<br>

<img src="https://github.com/user-attachments/assets/5e62f1c9-e5a7-41f2-9f4d-b69879cfdb7e" alt="image" style="width: 600px; height: auto;">

<br><br>

## 创建**Coze**工作流

<br>

首先登录到[coze](https://coze.cn),找到**个人空间**，在右上角找到并点击**创建Bot**，这个我们稍后会用到。这里需要你创建一个**工作流**，和**数据集**

<img src="https://github.com/user-attachments/assets/6d1f2b08-62d7-46d3-bdc8-9d95c0cc1f67" alt="image" style="width: 600px; height: auto;">

<br>

<img src="https://github.com/user-attachments/assets/7316a673-c883-42ad-bc79-a62a5f9e1d84" alt="image" style="width: 1000px; height: auto;">

<br>

<img src="https://github.com/user-attachments/assets/4ac4ba06-3a1d-4527-bf00-790f19dd2be5" alt="image" style="width: 1000px; height: auto;">

<br><br>

## 获取**CozeAPI**

好的你现在已经掌握了基本技巧，现在开始获取coze**api**,找到主页点击左下角**CozeAPI**

<br>

<img src="https://github.com/user-attachments/assets/33c8fd06-fa1a-4941-8bfe-94057ff056e2" alt="image" style="width: 600px; height: auto;">

<br>

创建**api**，请确保**只有你自己知道**，请注意保存，这个**只能复制一次**

<img src="https://github.com/user-attachments/assets/37ec8de2-ad83-46bd-a11b-f2d4573fd6a3" alt="image" style="width: 600px; height: auto;">

<br><br>

## 设置**CozeBot**

<br>

现在要编辑**客服机器人**，找到你刚刚创建的**机器人**，设置为**Agent （工作流模式）**,并且添加你创建的**工作流**

<img src="https://github.com/user-attachments/assets/2f767492-992b-49f2-9f64-090c1ed1d65b" alt="image" style="width: 600px; height: auto;">


## 待开发

- 对接多维表，数据实时同步至多维表（瀚中，8月22日）
- 优化问题
  - 优化问句判断方案及其速度
  - 优化代码，分模块编写，增加可阅读性和开发便利性
  - ...
- 数据集训练
  - 问答数据准确度达到75%（尹航，8月22日）
- 增加敏感词过滤模块

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=anuraghazra&layout=donut-vertical&langs_count=5&custom_title=Most%20Used%20Languages)](https://github.com/anuraghazra/github-readme-stats)

