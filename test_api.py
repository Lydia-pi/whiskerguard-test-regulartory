import requests
import json
from datetime import datetime
import random
import string

def generate_random_string(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# 配置
BASE_URL = "http://175.27.251.251:8080"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTc0NjAwMzUxOCwiYXV0aCI6IlJPTEVfQURNSU4gUk9MRV9VU0VSIiwiaWF0IjoxNzQ1OTE3MTE4fQ.3G3KYqJRMQZEqHzC1RKeodwahhm8VuDAQevBAIzkGb6SQTqyQ6BQRy_aJIyV6dA5-JaCfNDxbxGxc-PUeJRG8g"
}

# 生成唯一的类别名称
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
random_suffix = generate_random_string()
category_name = f"企业法规_{timestamp}_{random_suffix}"

# 准备请求数据
payload = {
    "tenantId": 9007199254740991,
    "categoryName": category_name,
    "parentId": None,
    "description": "123456",
    "createdAt": "2025-04-27T10:10:23.864Z",
    "updatedAt": "2025-04-27T10:10:23.864Z"
}

# 发送请求
url = f"{BASE_URL}/services/whiskerguardregulatoryservice/api/enterprise/categories/create"
print(f"\n请求URL: {url}")
print(f"请求头: {json.dumps(headers, indent=2)}")
print(f"请求体: {json.dumps(payload, indent=2)}")

response = requests.post(url, headers=headers, json=payload)

print(f"\n响应状态码: {response.status_code}")
print(f"响应内容: {response.text}") 