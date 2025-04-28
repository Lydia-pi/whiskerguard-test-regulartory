import pytest
import requests
import allure
import os
import logging
from datetime import datetime
import random
import string

# BASE_URL 和 Token 从环境变量读取，提升安全性
BASE_URL = os.getenv("BASE_URL", "http://175.27.251.251:8080")
AUTH_TOKEN = os.getenv("AUTH_TOKEN", "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTc0NTkyMzgzMSwiYXV0aCI6IlJPTEVfQURNSU4gUk9MRV9VU0VSIiwiaWF0IjoxNzQ1ODM3NDMxfQ.k6SQR5-cTgy7A1mecKPymn1fm62Vbului7yacDz_ZgI4EKsx9R58wv6KrDBJMXev2V3I3WfNr_HNzGOd2K5ztA")
AUTH_HEADER = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {AUTH_TOKEN}"
}

# 配置 logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def build_payload():
    now = datetime.now().isoformat()
    random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return {
        "tenantId": 9007199254740991,
        "categoryName": f"cat_{random_str}",
        #"parentId": null,
        "description": "123456"
        #"createdAt": now,
        #"updatedAt": now
    }

@allure.feature("法律法规管理服务-企业内部制度类别")
class TestEnterpriseCategory:

    @allure.story("添加企业内部法规分类")
    @pytest.mark.parametrize("payload, expected_code", [
        (
            build_payload(),
            201
        )
    ])
    def test_add_enterprise_category(self, payload, expected_code):
        url = f"{BASE_URL}/services/whiskerguardregulatoryservice/api/enterprise/categories/create"
        try:
            response = requests.post(url, json=payload, headers=AUTH_HEADER)
        except requests.RequestException as e:
            logging.error(f"请求异常: {e}")
            pytest.fail(f"请求异常: {e}")

        # 调试输出用 logging
        logging.info(f"URL: {url}")
        logging.info(f"返回码: {response.status_code}")
        logging.info(f"返回体: {response.text}")
        print("接口返回内容:", repr(response.text))

        # 断言
        assert response.status_code == expected_code

        # 断言业务字段
        try:
            data = response.json()
            assert "id" in data
            assert data.get("categoryName") == payload["categoryName"]
        except ValueError:
            pytest.fail(f"返回内容不是 JSON 格式: {response.text}")

