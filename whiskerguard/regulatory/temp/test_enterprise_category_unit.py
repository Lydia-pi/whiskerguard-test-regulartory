import unittest
import json
import pytest
import allure
import requests
from datetime import datetime
from whiskerguard.regulatory.config import ApiPaths, TestConfig
from whiskerguard.regulatory.utils import TestDataBuilder

@allure.epic("WhiskerGuard Regulatory")
@allure.feature("Enterprise Category Management")
class TestEnterpriseCategory(unittest.TestCase):
    def setUp(self):
        self.base_url = TestConfig.BASE_URL
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {TestConfig.AUTH_TOKEN}"
        }
        self.test_data = TestDataBuilder()
        self.tenant_id = 9007199254740991
        print(f"\n当前使用的请求头: {self.headers}")

    def create_category(self, category_name):
        """创建一个分类并返回其ID"""
        payload = {
            "tenantId": self.tenant_id,
            "categoryName": category_name,
            "parentId": None,
            "description": "测试描述"
        }
        response = requests.post(
            f"{self.base_url}{ApiPaths.ENTERPRISE_CATEGORY['CREATE']}",
            headers=self.headers,
            json=payload
        )
        self.assertEqual(response.status_code, 201)
        return response.json()['id']

    @allure.story("创建分类")
    @allure.title("缺少必填字段-失败场景")
    def test_create_category_missing_fields(self):
        payload = {}
        response = requests.post(
            f"{self.base_url}{ApiPaths.ENTERPRISE_CATEGORY['CREATE']}",
            headers=self.headers,
            json=payload
        )
        self.assertEqual(response.status_code, 400)

    @allure.story("创建分类")
    @allure.title("成功创建分类")
    def test_create_enterprise_category_success(self):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        category_name = f"企业法规_{timestamp}"
        payload = {
            "tenantId": self.tenant_id,
            "categoryName": category_name,
            "parentId": None,
            "description": "测试描述"
        }
        response = requests.post(
            f"{self.base_url}{ApiPaths.ENTERPRISE_CATEGORY['CREATE']}",
            headers=self.headers,
            json=payload
        )
        print(f"\n请求URL: {self.base_url}{ApiPaths.ENTERPRISE_CATEGORY['CREATE']}")
        print(f"请求体: {json.dumps(payload, indent=2)}")
        print(f"响应状态码: {response.status_code}")
        print(f"响应内容: {response.text}")
        
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIn('id', response_data)
        return response_data['id']

    @allure.story("更新分类")
    @allure.title("更新分类-成功场景")
    def test_update_category_success(self):
        # 先创建一个分类
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        category_name = f"企业法规_{timestamp}"
        category_id = self.create_category(category_name)
        
        # 然后更新这个分类
        new_category_name = f"企业法规_{timestamp}_updated"
        payload = {
            "id": category_id,
            "tenantId": self.tenant_id,
            "categoryName": new_category_name,
            "parentId": None,
            "description": "更新的测试描述"
        }
        response = requests.post(
            f"{self.base_url}{ApiPaths.ENTERPRISE_CATEGORY['UPDATE'].format(id=category_id)}",
            headers=self.headers,
            json=payload
        )
        print(f"\n更新请求URL: {self.base_url}{ApiPaths.ENTERPRISE_CATEGORY['UPDATE'].format(id=category_id)}")
        print(f"更新请求体: {json.dumps(payload, indent=2)}")
        print(f"更新响应状态码: {response.status_code}")
        print(f"更新响应内容: {response.text}")
        
        self.assertEqual(response.status_code, 200)

    @allure.story("部分更新分类")
    @allure.title("部分更新分类-成功场景")
    def test_partial_update_category(self):
        # 先创建一个分类
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        category_name = f"企业法规_{timestamp}"
        category_id = self.create_category(category_name)
        
        # 然后部分更新这个分类
        new_category_name = f"企业法规_{timestamp}_partial"
        payload = {
            "id": category_id,
            "categoryName": new_category_name,
            "tenantId": self.tenant_id
        }
        response = requests.post(
            f"{self.base_url}{ApiPaths.ENTERPRISE_CATEGORY['PARTIAL_UPDATE'].format(id=category_id)}",
            headers=self.headers,
            json=payload
        )
        print(f"\n部分更新请求URL: {self.base_url}{ApiPaths.ENTERPRISE_CATEGORY['PARTIAL_UPDATE'].format(id=category_id)}")
        print(f"部分更新请求体: {json.dumps(payload, indent=2)}")
        print(f"部分更新响应状态码: {response.status_code}")
        print(f"部分更新响应内容: {response.text}")
        
        self.assertEqual(response.status_code, 200)

    @allure.story("获取分类")
    @allure.title("获取单个分类")
    def test_get_category(self):
        # 先创建一个分类
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        category_name = f"企业法规_{timestamp}"
        category_id = self.create_category(category_name)
        
        response = requests.get(
            f"{self.base_url}{ApiPaths.ENTERPRISE_CATEGORY['GET_BY_ID'].format(id=category_id)}",
            headers=self.headers,
            params={'tenantId': self.tenant_id}  # 添加 tenantId 参数
        )
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIn('id', response_data)
        self.assertEqual(response_data['id'], category_id)

    @allure.story("获取分类树")
    @allure.title("获取分类树结构")
    def test_get_category_tree(self):
        response = requests.get(
            f"{self.base_url}{ApiPaths.ENTERPRISE_CATEGORY['TREE']}",
            headers=self.headers,
            params={'tenantId': self.tenant_id}  # 添加 tenantId 参数
        )
        print(f"\n获取分类树请求URL: {self.base_url}{ApiPaths.ENTERPRISE_CATEGORY['TREE']}")
        print(f"获取分类树响应状态码: {response.status_code}")
        print(f"获取分类树响应内容: {response.text}")
        
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIsInstance(response_data, list)

    @allure.story("删除分类")
    @allure.title("成功删除分类")
    def test_delete_category_success(self):
        # 先创建一个分类
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        category_name = f"企业法规_{timestamp}"
        category_id = self.create_category(category_name)
        
        response = requests.get(
            f"{self.base_url}{ApiPaths.ENTERPRISE_CATEGORY['DELETE'].format(id=category_id)}",
            headers=self.headers,
            params={'tenantId': self.tenant_id}  # 添加 tenantId 参数
        )
        print(f"\n删除请求URL: {self.base_url}{ApiPaths.ENTERPRISE_CATEGORY['DELETE'].format(id=category_id)}")
        print(f"删除响应状态码: {response.status_code}")
        
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main() 