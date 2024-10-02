import lark_oapi as lark

# 创建client
client = lark.Client.builder().app_id("APP_ID").app_secret("APP_SECRET").build()

# 构造请求对象
request = lark.contact.v3.GetUserRequest.builder().user_id("7be5fg9a").build()

# 发起请求
response = client.contact.v3.user.get(request)