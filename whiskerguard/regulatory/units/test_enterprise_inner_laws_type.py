import unittest
import requests
import os
from .config import BASE_URL, HEADERS, TEST_DATA, ENV, PORT

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
        
    def test_01_create_category(self):
        """测试创建企业内部法规分类"""
        url = f"{self.base_url}/enterprise/categories/create"
        response = requests.post(url, json=self.test_data, headers=self.headers)
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
            
        url = f"{self.base_url}/enterprise/categories/get/{self.category_id}"
        response = requests.get(url, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["name"], self.test_data["name"])
        self.assertEqual(data["code"], self.test_data["code"])
        
    def test_03_update_category(self):
        """测试更新企业内部法规分类"""
        # 先创建分类
        if not self.category_id:
            self.category_id = self.test_01_create_category()
            
        # 更新数据
        update_data = self.test_data.copy()
        update_data["name"] = "更新后的企业法规分类"
        update_data["description"] = "更新后的描述"
        
        url = f"{self.base_url}/enterprise/categories/update/{self.category_id}"
        response = requests.post(url, json=update_data, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["name"], update_data["name"])
        self.assertEqual(data["description"], update_data["description"])
        
    def test_04_partial_update_category(self):
        """测试部分更新企业内部法规分类"""
        # 先创建分类
        if not self.category_id:
            self.category_id = self.test_01_create_category()
            
        # 部分更新数据
        partial_update_data = {"name": "部分更新后的企业法规分类"}
        
        url = f"{self.base_url}/enterprise/categories/partialUpdate/{self.category_id}"
        response = requests.post(url, json=partial_update_data, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["name"], partial_update_data["name"])
        
    def test_05_get_category_tree(self):
        """测试获取企业内部法规分类树"""
        url = f"{self.base_url}/enterprise/categories/tree"
        response = requests.get(url, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        
    def test_06_delete_category(self):
        """测试删除企业内部法规分类"""
        # 先创建分类
        if not self.category_id:
            self.category_id = self.test_01_create_category()
            
        url = f"{self.base_url}/enterprise/categories/delete/{self.category_id}"
        response = requests.get(url, headers=self.headers)
        self.assertEqual(response.status_code, 204)
        
        # 验证删除后无法获取
        url = f"{self.base_url}/enterprise/categories/get/{self.category_id}"
        response = requests.get(url, headers=self.headers)
        self.assertEqual(response.status_code, 404)
        
if __name__ == "__main__":
    unittest.main() 