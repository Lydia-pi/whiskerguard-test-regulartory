import unittest
import json
from datetime import datetime
from whiskerguard.regulatory.utils import TestUtils, TestDataBuilder
from whiskerguard.regulatory.config import ApiPaths, TestConfig

class ComplianceCaseUser:
    """合规案例管理接口测试类"""
    
    def __init__(self):
        self.test_utils = TestUtils()
        self.test_data_builder = TestDataBuilder()
        self.base_url = TestConfig.BASE_URL
        self.headers = TestConfig.HEADERS
        
    def create_compliance_case(self, payload=None):
        """创建合规案例"""
        if payload is None:
            payload = self.test_data_builder.build_compliance_case_payload()
            
        url = self.test_utils.build_url(ApiPaths.COMPLIANCE_CASE.CREATE)
        response = self.test_utils.make_request('POST', url, json=payload, headers=self.headers)
        return response
        
    def update_compliance_case(self, case_id, payload):
        """更新合规案例"""
        url = self.test_utils.build_url(ApiPaths.COMPLIANCE_CASE.UPDATE.format(id=case_id))
        response = self.test_utils.make_request('POST', url, json=payload, headers=self.headers)
        return response
        
    def get_compliance_case(self, case_id):
        """获取单个合规案例"""
        url = self.test_utils.build_url(ApiPaths.COMPLIANCE_CASE.GET.format(id=case_id))
        response = self.test_utils.make_request('GET', url, headers=self.headers)
        return response
        
    def delete_compliance_case(self, case_id):
        """删除合规案例"""
        url = self.test_utils.build_url(ApiPaths.COMPLIANCE_CASE.DELETE.format(id=case_id))
        response = self.test_utils.make_request('DELETE', url, headers=self.headers)
        return response
        
    def get_compliance_cases_page(self, page=0, size=20, query_params=None):
        """分页查询合规案例"""
        if query_params is None:
            query_params = {}
            
        url = self.test_utils.build_url(ApiPaths.COMPLIANCE_CASE.PAGE)
        params = {
            'page': page,
            'size': size,
            **query_params
        }
        response = self.test_utils.make_request('POST', url, json=params, headers=self.headers)
        return response

class TestComplianceCase(unittest.TestCase):
    """合规案例管理接口测试用例"""
    
    def setUp(self):
        """测试前置"""
        self.compliance_case = ComplianceCaseUser()
        self.test_data_builder = TestDataBuilder()
        
    def test_01_create_compliance_case_success(self):
        """测试创建合规案例-成功"""
        # 准备测试数据
        payload = self.test_data_builder.build_compliance_case_payload()
        
        # 发送请求
        response = self.compliance_case.create_compliance_case(payload)
        
        # 断言
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        self.assertIsNotNone(response_data.get('id'))
        self.assertEqual(response_data.get('caseName'), payload.get('caseName'))
        self.assertEqual(response_data.get('caseCode'), payload.get('caseCode'))
        
        # 保存案例ID供后续测试使用
        self.case_id = response_data.get('id')
        
    def test_02_create_compliance_case_missing_required(self):
        """测试创建合规案例-缺少必填字段"""
        # 准备测试数据 - 缺少必填字段caseName
        payload = self.test_data_builder.build_compliance_case_payload()
        payload.pop('caseName')
        
        # 发送请求
        response = self.compliance_case.create_compliance_case(payload)
        
        # 断言
        self.assertEqual(response.status_code, 400)
        
    def test_03_update_compliance_case_success(self):
        """测试更新合规案例-成功"""
        # 准备测试数据
        update_payload = {
            'id': self.case_id,
            'caseName': '更新后的案例名称',
            'summary': '更新后的案例摘要'
        }
        
        # 发送请求
        response = self.compliance_case.update_compliance_case(self.case_id, update_payload)
        
        # 断言
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data.get('caseName'), update_payload.get('caseName'))
        self.assertEqual(response_data.get('summary'), update_payload.get('summary'))
        
    def test_04_update_compliance_case_not_exist(self):
        """测试更新合规案例-案例不存在"""
        # 准备测试数据
        update_payload = {
            'id': 99999,
            'caseName': '不存在的案例'
        }
        
        # 发送请求
        response = self.compliance_case.update_compliance_case(99999, update_payload)
        
        # 断言
        self.assertEqual(response.status_code, 404)
        
    def test_05_get_compliance_case_success(self):
        """测试获取单个合规案例-成功"""
        # 发送请求
        response = self.compliance_case.get_compliance_case(self.case_id)
        
        # 断言
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data.get('id'), self.case_id)
        
    def test_06_get_compliance_case_not_exist(self):
        """测试获取单个合规案例-案例不存在"""
        # 发送请求
        response = self.compliance_case.get_compliance_case(99999)
        
        # 断言
        self.assertEqual(response.status_code, 404)
        
    def test_07_get_compliance_cases_page_success(self):
        """测试分页查询合规案例-成功"""
        # 准备查询参数
        query_params = {
            'caseName': '更新后的案例名称',
            'areaType': 'INDUSTRY_REGULATION'
        }
        
        # 发送请求
        response = self.compliance_case.get_compliance_cases_page(query_params=query_params)
        
        # 断言
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIsNotNone(response_data.get('content'))
        self.assertGreater(len(response_data.get('content')), 0)
        
    def test_08_get_compliance_cases_page_empty(self):
        """测试分页查询合规案例-空结果"""
        # 准备查询参数 - 使用不存在的案例名称
        query_params = {
            'caseName': '不存在的案例名称'
        }
        
        # 发送请求
        response = self.compliance_case.get_compliance_cases_page(query_params=query_params)
        
        # 断言
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(len(response_data.get('content')), 0)
        
    def test_09_delete_compliance_case_success(self):
        """测试删除合规案例-成功"""
        # 发送请求
        response = self.compliance_case.delete_compliance_case(self.case_id)
        
        # 断言
        self.assertEqual(response.status_code, 204)
        
        # 验证删除后无法获取
        get_response = self.compliance_case.get_compliance_case(self.case_id)
        self.assertEqual(get_response.status_code, 404)
        
    def test_10_delete_compliance_case_not_exist(self):
        """测试删除合规案例-案例不存在"""
        # 发送请求
        response = self.compliance_case.delete_compliance_case(99999)
        
        # 断言
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main() 