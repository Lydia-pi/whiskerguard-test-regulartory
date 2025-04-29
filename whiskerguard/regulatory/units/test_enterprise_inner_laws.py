import unittest
import requests
import os
from .config import BASE_URL, HEADERS, TEST_DATA, ENV, PORT

class TestEnterpriseInnerLaws(unittest.TestCase):
    """企业内部法规管理测试类"""
    
    @classmethod
    def setUpClass(cls):
        """测试类初始化，打印环境信息"""
        print(f"\n开始测试企业内部法规管理 - 环境: {ENV}, 端口: {PORT}")
        
    def setUp(self):
        """测试前的准备工作"""
        self.base_url = BASE_URL
        self.headers = HEADERS
        self.test_data = TEST_DATA["enterprise_regulation"]
        self.regulation_id = None
        self.category_id = None
        
    def test_01_create_category(self):
        """测试创建企业内部法规分类（用于后续测试）"""
        url = f"{self.base_url}/enterprise/categories/create"
        response = requests.post(url, json=TEST_DATA["enterprise_category"], headers=self.headers)
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertIn("id", data)
        self.category_id = data["id"]
        return self.category_id
        
    def test_02_create_regulation(self):
        """测试创建企业内部法规"""
        # 先创建分类
        if not self.category_id:
            self.category_id = self.test_01_create_category()
            
        # 设置分类ID
        self.test_data["categoryId"] = self.category_id
        
        url = f"{self.base_url}/enterprise/regulations/create"
        response = requests.post(url, json=self.test_data, headers=self.headers)
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertIn("id", data)
        self.regulation_id = data["id"]
        return self.regulation_id
        
    def test_03_get_regulation(self):
        """测试获取企业内部法规"""
        # 先创建法规
        if not self.regulation_id:
            self.regulation_id = self.test_02_create_regulation()
            
        url = f"{self.base_url}/enterprise/regulations/get/{self.regulation_id}"
        response = requests.get(url, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["title"], self.test_data["title"])
        self.assertEqual(data["content"], self.test_data["content"])
        
    def test_04_update_regulation(self):
        """测试更新企业内部法规"""
        # 先创建法规
        if not self.regulation_id:
            self.regulation_id = self.test_02_create_regulation()
            
        # 更新数据
        update_data = self.test_data.copy()
        update_data["title"] = "更新后的企业法规"
        update_data["content"] = "更新后的内容"
        
        url = f"{self.base_url}/enterprise/regulations/update/{self.regulation_id}"
        response = requests.post(url, json=update_data, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["title"], update_data["title"])
        self.assertEqual(data["content"], update_data["content"])
        
    def test_05_get_regulation_page(self):
        """测试分页查询企业内部法规"""
        url = f"{self.base_url}/enterprise/regulations/page"
        params = {"page": 0, "size": 10}
        response = requests.get(url, params=params, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("content", data)
        self.assertIsInstance(data["content"], list)
        
    def test_06_delete_regulation(self):
        """测试删除企业内部法规"""
        # 先创建法规
        if not self.regulation_id:
            self.regulation_id = self.test_02_create_regulation()
            
        url = f"{self.base_url}/enterprise/regulations/delete/{self.regulation_id}"
        response = requests.get(url, headers=self.headers)
        self.assertEqual(response.status_code, 204)
        
        # 验证删除后无法获取
        url = f"{self.base_url}/enterprise/regulations/get/{self.regulation_id}"
        response = requests.get(url, headers=self.headers)
        self.assertEqual(response.status_code, 404)
        
    def test_07_batch_publish_regulations(self):
        """测试批量发布企业内部法规"""
        # 先创建多个法规
        regulation_ids = []
        for i in range(3):
            regulation_id = self.test_02_create_regulation()
            regulation_ids.append(regulation_id)
            
        url = f"{self.base_url}/enterprise/regulations/publish/batch"
        response = requests.post(url, json=regulation_ids, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        
if __name__ == "__main__":
    unittest.main() 