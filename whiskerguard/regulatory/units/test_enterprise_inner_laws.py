import unittest
import requests
import os
from datetime import datetime, timezone
from .config import BASE_URL, HEADERS, TEST_DATA, ENV, PORT, ApiPaths

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
        self.test_data = TEST_DATA["enterprise_regulation"].copy()
        current_time = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        self.test_data.update({
            "tenantId": 1,
            "regulationCode": f"REG_{datetime.now().strftime('%Y%m%d%H%M%S')}",
            "type": "REGULATION",
            "status": "DRAFT",
            "version": "1.0",
            "effectiveDate": current_time,
            "expireDate": "2099-12-31",
            "publishStatus": "UNPUBLISHED",
            "description": "测试描述",
            "keywords": ["测试", "关键词"],
            "attachments": [],
            "department": "测试部门",
            "summary": "测试摘要"
        })
        self.regulation_id = None
        self.category_id = None
        self._clean_existing_data()
        
    def _clean_existing_data(self):
        """清理已存在的测试数据"""
        # 清理法规
        url = f"{self.base_url}{ApiPaths.ENTERPRISE_REGULATION['PAGE']}"
        params = {
            "page": 0,
            "size": 100,
            "tenantId": 1,
            "sort": ["id,desc"]
        }
        response = requests.post(url, json=params, headers=self.headers)
        if response.status_code == 200:
            regulations = response.json().get("content", [])
            for regulation in regulations:
                delete_url = f"{self.base_url}{ApiPaths.ENTERPRISE_REGULATION['DELETE'].format(id=regulation['id'])}"
                requests.get(delete_url, headers=self.headers)
                
        # 清理分类
        url = f"{self.base_url}{ApiPaths.ENTERPRISE_CATEGORY['TREE']}"
        params = {"tenantId": 1}
        response = requests.get(url, params=params, headers=self.headers)
        if response.status_code == 200:
            categories = response.json()
            for category in categories:
                delete_url = f"{self.base_url}{ApiPaths.ENTERPRISE_CATEGORY['DELETE'].format(id=category['id'])}"
                requests.get(delete_url, headers=self.headers)
        
    def test_01_create_category(self):
        """测试创建企业内部法规分类（用于后续测试）"""
        url = f"{self.base_url}{ApiPaths.ENTERPRISE_CATEGORY['CREATE']}"
        response = requests.post(url, json=TEST_DATA["enterprise_category"], headers=self.headers)
        print(f"创建分类请求URL: {url}")
        print(f"请求数据: {TEST_DATA['enterprise_category']}")
        print(f"响应状态码: {response.status_code}")
        print(f"响应内容: {response.text}")
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
        
        # 移除可能导致问题的字段
        create_data = self.test_data.copy()
        for field in ["createdAt", "updatedAt", "createdBy", "updatedBy"]:
            create_data.pop(field, None)
        
        url = f"{self.base_url}{ApiPaths.ENTERPRISE_REGULATION['CREATE']}"
        response = requests.post(url, json=create_data, headers=self.headers)
        print(f"创建法规请求URL: {url}")
        print(f"请求数据: {create_data}")
        print(f"响应状态码: {response.status_code}")
        print(f"响应内容: {response.text}")
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
            
        url = f"{self.base_url}{ApiPaths.ENTERPRISE_REGULATION['GET_BY_ID'].format(id=self.regulation_id)}"
        response = requests.get(url, headers=self.headers)
        print(f"获取法规请求URL: {url}")
        print(f"响应状态码: {response.status_code}")
        print(f"响应内容: {response.text}")
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
        update_data["id"] = self.regulation_id
        
        # 移除可能导致问题的字段
        for field in ["createdAt", "updatedAt", "createdBy", "updatedBy"]:
            update_data.pop(field, None)
        
        url = f"{self.base_url}{ApiPaths.ENTERPRISE_REGULATION['UPDATE'].format(id=self.regulation_id)}"
        response = requests.post(url, json=update_data, headers=self.headers)
        print(f"更新法规请求URL: {url}")
        print(f"请求数据: {update_data}")
        print(f"响应状态码: {response.status_code}")
        print(f"响应内容: {response.text}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["title"], update_data["title"])
        self.assertEqual(data["content"], update_data["content"])
        
    def test_05_get_regulation_page(self):
        """测试分页查询企业内部法规"""
        url = f"{self.base_url}{ApiPaths.ENTERPRISE_REGULATION['PAGE']}"
        params = {
            "page": 0,
            "size": 10,
            "tenantId": 1,
            "sort": ["id,desc"]
        }
        response = requests.post(url, json=params, headers=self.headers)
        print(f"分页查询请求URL: {url}")
        print(f"请求参数: {params}")
        print(f"响应状态码: {response.status_code}")
        print(f"响应内容: {response.text}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("content", data)
        self.assertIsInstance(data["content"], list)
        
    def test_06_delete_regulation(self):
        """测试删除企业内部法规"""
        # 先创建法规
        if not self.regulation_id:
            self.regulation_id = self.test_02_create_regulation()
            
        url = f"{self.base_url}{ApiPaths.ENTERPRISE_REGULATION['DELETE'].format(id=self.regulation_id)}"
        response = requests.get(url, headers=self.headers)
        print(f"删除法规请求URL: {url}")
        print(f"响应状态码: {response.status_code}")
        print(f"响应内容: {response.text}")
        self.assertEqual(response.status_code, 204)
        
        # 验证删除后无法获取
        url = f"{self.base_url}{ApiPaths.ENTERPRISE_REGULATION['GET_BY_ID'].format(id=self.regulation_id)}"
        response = requests.get(url, headers=self.headers)
        self.assertEqual(response.status_code, 404)
        
    def test_07_batch_publish_regulations(self):
        """测试批量发布企业内部法规"""
        # 先创建多个法规
        regulation_ids = []
        for i in range(3):
            regulation_id = self.test_02_create_regulation()
            regulation_ids.append(regulation_id)
            
        url = f"{self.base_url}{ApiPaths.ENTERPRISE_REGULATION['BATCH_PUBLISH']}"
        response = requests.post(url, json=regulation_ids, headers=self.headers)
        print(f"批量发布请求URL: {url}")
        print(f"请求数据: {regulation_ids}")
        print(f"响应状态码: {response.status_code}")
        print(f"响应内容: {response.text}")
        self.assertEqual(response.status_code, 200)
        
if __name__ == "__main__":
    unittest.main() 