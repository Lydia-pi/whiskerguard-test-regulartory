import unittest
import requests
import os
from whiskerguard.regulatory.units.config import BASE_URL, HEADERS, TEST_DATA, ApiPaths

class TestLawsType(unittest.TestCase):
    """法律法规分类管理测试类"""
    
    @classmethod
    def setUpClass(cls):
        """测试类初始化，打印环境信息"""
        print(f"\n开始测试法律法规分类管理")
        
    def setUp(self):
        """测试前的准备工作"""
        self.base_url = BASE_URL
        self.headers = HEADERS
        self.test_data = TEST_DATA["laws_category"]
        self.category_id = None
        
    def test_01_create_category(self):
        """测试创建法律法规分类"""
        url = f"{self.base_url}{ApiPaths.LAW_CATEGORY['CREATE']}"
        response = requests.post(url, json=self.test_data, headers=self.headers)
        print(f"\n创建分类请求URL: {url}")
        print(f"请求数据: {self.test_data}")
        print(f"响应状态码: {response.status_code}")
        print(f"响应内容: {response.text}")
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertIn("id", data)
        self.category_id = data["id"]
        return self.category_id
        
    def test_02_get_category(self):
        """测试获取法律法规分类"""
        # 先创建分类
        if not self.category_id:
            self.category_id = self.test_01_create_category()
            
        url = f"{self.base_url}{ApiPaths.LAW_CATEGORY['GET_BY_ID'].format(id=self.category_id)}"
        response = requests.get(url, headers=self.headers)
        print(f"\n获取分类请求URL: {url}")
        print(f"响应状态码: {response.status_code}")
        print(f"响应内容: {response.text}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["categoryName"], self.test_data["categoryName"])
        
    def test_03_partial_update_category(self):
        """测试部分更新法律法规分类"""
        # 使用指定的ID
        self.category_id = 17
            
        # 部分更新数据
        partial_update_data = {"categoryName": "部分更新后的法律法规分类"}
        
        url = f"{self.base_url}{ApiPaths.LAW_CATEGORY['PARTIAL_UPDATE'].format(id=self.category_id)}"
        response = requests.post(url, json=partial_update_data, headers=self.headers)
        print(f"\n部分更新分类请求URL: {url}")
        print(f"请求数据: {partial_update_data}")
        print(f"响应状态码: {response.status_code}")
        print(f"响应内容: {response.text}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["categoryName"], partial_update_data["categoryName"])
        
    def test_04_get_category_page(self):
        """测试分页获取法律法规分类"""
        url = f"{self.base_url}{ApiPaths.LAW_CATEGORY['PAGE']}"
        params = {"page": 0, "size": 10}
        response = requests.get(url, params=params, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("content", data)
        self.assertIsInstance(data["content"], list)
        
    def test_05_delete_category(self):
        """测试删除法律法规分类"""
        # 先创建分类
        if not self.category_id:
            self.category_id = self.test_01_create_category()
            
        url = f"{self.base_url}{ApiPaths.LAW_CATEGORY['DELETE'].format(id=self.category_id)}"
        response = requests.get(url, headers=self.headers)
        print(f"\n删除分类请求URL: {url}")
        print(f"响应状态码: {response.status_code}")
        print(f"响应内容: {response.text}")
        self.assertEqual(response.status_code, 204)
        
        # 验证删除后无法获取
        url = f"{self.base_url}{ApiPaths.LAW_CATEGORY['GET_BY_ID'].format(id=self.category_id)}"
        response = requests.get(url, headers=self.headers)
        self.assertEqual(response.status_code, 404)
        
    def test_06_get_category_tree(self):
        """测试获取法律法规分类树"""
        url = f"{self.base_url}{ApiPaths.LAW_CATEGORY['TREE']}"
        response = requests.get(url, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        
if __name__ == "__main__":
    unittest.main() 