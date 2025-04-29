import unittest
import requests
import os
from .config import BASE_URL, HEADERS, TEST_DATA, ENV, PORT, ApiPaths

class TestEnterpriseInnerLawsType(unittest.TestCase):
    """企业内部法规分类管理测试类"""
    
    @classmethod
    def setUpClass(cls):
        """测试类初始化，打印环境信息"""
        print(f"\n开始测试企业内部法规分类管理 - 环境: {ENV}, 端口: {PORT}")
        
    def setUp(self):
        """测试前的准备工作"""
        self.base_url = BASE_URL
        self.headers = HEADERS
        self.test_data = TEST_DATA["enterprise_category"]
        self.category_id = None
        self._clean_existing_categories()
        
    def _clean_existing_categories(self):
        """清理已存在的分类"""
        # 获取所有分类
        url = f"{self.base_url}{ApiPaths.ENTERPRISE_CATEGORY['TREE']}"
        params = {"tenantId": 1}
        response = requests.get(url, params=params, headers=self.headers)
        if response.status_code == 200:
            categories = response.json()
            # 删除所有分类
            for category in categories:
                delete_url = f"{self.base_url}{ApiPaths.ENTERPRISE_CATEGORY['DELETE'].format(id=category['id'])}"
                requests.get(delete_url, headers=self.headers)
        
    def test_01_create_category(self):
        """测试创建企业内部法规分类"""
        test_data = self.test_data.copy()
        test_data["categoryName"] = f"测试企业法规分类_{self._testMethodName}"
        test_data["categoryCode"] = f"TEST_CATEGORY_{self._testMethodName}"
        
        url = f"{self.base_url}{ApiPaths.ENTERPRISE_CATEGORY['CREATE']}"
        print(f"创建分类请求URL: {url}")
        print(f"请求数据: {test_data}")
        response = requests.post(url, json=test_data, headers=self.headers)
        print(f"响应状态码: {response.status_code}")
        print(f"响应内容: {response.text}")
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertIn("id", data)
        self.category_id = data["id"]
        return self.category_id
        
    def test_02_get_category(self):
        """测试获取企业内部法规分类"""
        # 先创建分类
        if not self.category_id:
            self.category_id = self.test_01_create_category()
            
        url = f"{self.base_url}{ApiPaths.ENTERPRISE_CATEGORY['GET_BY_ID'].format(id=self.category_id)}"
        response = requests.get(url, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["categoryName"], f"测试企业法规分类_{self._testMethodName}")
        
    def test_03_update_category(self):
        """测试更新企业内部法规分类"""
        # 先创建分类
        if not self.category_id:
            self.category_id = self.test_01_create_category()
            
        # 更新数据
        update_data = self.test_data.copy()
        update_data["categoryName"] = "更新后的企业法规分类"
        update_data["description"] = "更新后的描述"
        update_data["id"] = self.category_id
        update_data["tenantId"] = 1
        
        url = f"{self.base_url}{ApiPaths.ENTERPRISE_CATEGORY['PARTIAL_UPDATE'].format(id=self.category_id)}"
        response = requests.post(url, json=update_data, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["categoryName"], update_data["categoryName"])
        self.assertEqual(data["description"], update_data["description"])
        
    def test_04_partial_update_category(self):
        """测试部分更新企业内部法规分类"""
        # 先创建分类
        if not self.category_id:
            self.category_id = self.test_01_create_category()
            
        # 部分更新数据
        partial_update_data = {
            "id": self.category_id,
            "tenantId": 1,
            "categoryName": "部分更新后的企业法规分类"
        }
        
        url = f"{self.base_url}{ApiPaths.ENTERPRISE_CATEGORY['PARTIAL_UPDATE'].format(id=self.category_id)}"
        response = requests.post(url, json=partial_update_data, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["categoryName"], partial_update_data["categoryName"])
        
    def test_05_get_category_tree(self):
        """测试获取企业内部法规分类树"""
        url = f"{self.base_url}{ApiPaths.ENTERPRISE_CATEGORY['TREE']}"
        params = {"tenantId": 1}
        response = requests.get(url, params=params, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        
    def test_06_delete_category(self):
        """测试删除企业内部法规分类"""
        # 先创建分类
        if not self.category_id:
            self.category_id = self.test_01_create_category()
            
        url = f"{self.base_url}{ApiPaths.ENTERPRISE_CATEGORY['DELETE'].format(id=self.category_id)}"
        response = requests.get(url, headers=self.headers)
        self.assertEqual(response.status_code, 204)
        
        # 验证删除后无法获取
        url = f"{self.base_url}{ApiPaths.ENTERPRISE_CATEGORY['GET_BY_ID'].format(id=self.category_id)}"
        response = requests.get(url, headers=self.headers)
        self.assertEqual(response.status_code, 404)
        
if __name__ == "__main__":
    unittest.main() 