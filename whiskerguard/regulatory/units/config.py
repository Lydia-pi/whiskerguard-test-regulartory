import os

# 环境配置
ENV = os.getenv("REGULATORY_ENV", "dev")  # 默认为开发环境，可选值: dev, prod

# 认证配置
AUTH_TOKEN = "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTc0NjAwMzUxOCwiYXV0aCI6IlJPTEVfQURNSU4gUk9MRV9VU0VSIiwiaWF0IjoxNzQ1OTE3MTE4fQ.3G3KYqJRMQZEqHzC1RKeodwahhm8VuDAQevBAIzkGb6SQTqyQ6BQRy_aJIyV6dA5-JaCfNDxbxGxc-PUeJRG8g"

# 请求头配置
HEADERS = {
    "Authorization": AUTH_TOKEN,
    "Content-Type": "application/json"
}

# 环境特定配置
if ENV == "prod":
    # 生产环境配置
    BASE_URL = os.getenv("REGULATORY_PROD_BASE_URL", "https://api.example.com/whiskerguardregulatoryservice/api")
    PORT = os.getenv("REGULATORY_PROD_PORT", "443")
else:
    # 开发环境配置
    BASE_URL = os.getenv("REGULATORY_DEV_BASE_URL", "http://175.27.251.251:8080/whiskerguardregulatoryservice/api")
    PORT = os.getenv("REGULATORY_DEV_PORT", "8080")

# API路径配置
class ApiPaths:
    LAW_CATEGORY = {
        "CREATE": "/laws/categories/create",
        "GET_BY_ID": "/laws/categories/get/{id}",
        "PARTIAL_UPDATE": "/laws/categories/update/{id}",
        "PAGE": "/laws/categories/page",
        "DELETE": "/laws/categories/delete/{id}",
        "TREE": "/laws/categories/tree"
    }
    
    ENTERPRISE_CATEGORY = {
        "CREATE": "/enterprise/categories/create",
        "GET_BY_ID": "/enterprise/categories/get/{id}",
        "PARTIAL_UPDATE": "/enterprise/categories/{id}/update",
        "PAGE": "/enterprise/categories/page",
        "DELETE": "/enterprise/categories/delete/{id}",
        "TREE": "/enterprise/categories/tree"
    }
    
    ENTERPRISE_REGULATION = {
        "CREATE": "/enterprise/regulations/create",
        "GET_BY_ID": "/enterprise/regulations/get/{id}",
        "UPDATE": "/enterprise/regulations/{id}/update",
        "PARTIAL_UPDATE": "/enterprise/regulations/{id}/update",
        "PAGE": "/enterprise/regulations/page",
        "DELETE": "/enterprise/regulations/delete/{id}",
        "BATCH_PUBLISH": "/enterprise/regulations/batch-publish"
    }

# 测试数据配置
TEST_DATA = {
    "enterprise_category": {
        "name": "测试企业法规分类",
        "code": "TEST_CATEGORY",
        "description": "用于测试的企业法规分类"
    },
    "laws_category": {
        "categoryName": "测试法律法规分类",
        "categoryCode": "TEST_LAWS_CATEGORY",
        "description": "用于测试的法律法规分类",
        "parentId": None,
        "status": "ENABLE"
    },
    "enterprise_regulation": {
        "title": "测试企业法规",
        "content": "测试内容",
        "categoryId": None,  # 将在测试中动态设置
        "type": "REGULATION",
        "status": "DRAFT"
    }
}

# 打印当前环境配置
print(f"当前环境: {ENV}")
print(f"API基础URL: {BASE_URL}")
print(f"端口: {PORT}") 