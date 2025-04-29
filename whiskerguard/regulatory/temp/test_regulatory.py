import unittest
import requests
from .config import BASE_URL, HEADERS, TEST_DATA

class TestRegulatoryService(unittest.TestCase):
    def setUp(self):
        """测试前的准备工作"""
        self.base_url = BASE_URL
        self.headers = HEADERS
        self.test_data = TEST_DATA
        
    def test_create_enterprise_category(self):
        """测试创建企业法规分类"""
        url = f"{self.base_url}/enterprise/categories"
        response = requests.post(url, json=self.test_data["enterprise_category"], headers=self.headers)
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertIn("id", data)
        return data["id"]
        
    def test_create_laws_category(self):
        """测试创建法律法规分类"""
        url = f"{self.base_url}/laws/categories"
        response = requests.post(url, json=self.test_data["laws_category"], headers=self.headers)
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertIn("id", data)
        return data["id"]
        
    def test_create_enterprise_regulation(self):
        """测试创建企业法规"""
        # 先创建分类
        category_id = self.test_create_enterprise_category()
        
        # 设置分类ID
        self.test_data["enterprise_regulation"]["categoryId"] = category_id
        
        url = f"{self.base_url}/enterprise/regulations"
        response = requests.post(url, json=self.test_data["enterprise_regulation"], headers=self.headers)
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertIn("id", data)
        return data["id"]
        
    def test_get_enterprise_regulation(self):
        """测试获取企业法规"""
        # 先创建法规
        regulation_id = self.test_create_enterprise_regulation()
        
        url = f"{self.base_url}/enterprise/regulations/{regulation_id}"
        response = requests.get(url, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["title"], self.test_data["enterprise_regulation"]["title"])
        
if __name__ == "__main__":
    unittest.main() 