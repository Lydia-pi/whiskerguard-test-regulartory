import requests
import logging
import random
import string
from datetime import datetime
from .config import BASE_URL, COMMON_HEADERS, LogConfig

# 配置日志
logging.basicConfig(
    level=getattr(logging, LogConfig.LEVEL),
    format=LogConfig.FORMAT,
    filename=LogConfig.FILE
)

class TestUtils:
    @staticmethod
    def generate_random_string(length=8):
        """生成随机字符串"""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    @staticmethod
    def get_current_timestamp():
        """获取当前时间戳"""
        return datetime.now().isoformat()

    @staticmethod
    def make_request(method, url, **kwargs):
        """统一的请求处理方法"""
        try:
            # 如果 kwargs 中已经包含 headers，则合并 headers
            if 'headers' in kwargs:
                headers = {**COMMON_HEADERS, **kwargs['headers']}
                kwargs['headers'] = headers
            else:
                kwargs['headers'] = COMMON_HEADERS
                
            # 记录请求信息
            logging.info(f"Request URL: {url}")
            logging.info(f"Request Method: {method}")
            logging.info(f"Request Headers: {kwargs.get('headers')}")
            if 'json' in kwargs:
                logging.info(f"Request Body: {kwargs.get('json')}")
            if 'params' in kwargs:
                logging.info(f"Request Params: {kwargs.get('params')}")
                
            response = requests.request(
                method=method,
                url=url,
                **kwargs
            )
            
            # 记录响应信息
            logging.info(f"Response Status: {response.status_code}")
            logging.info(f"Response Headers: {dict(response.headers)}")
            logging.info(f"Response Body: {response.text}")
            
            return response
        except Exception as e:
            logging.error(f"请求发生错误: {str(e)}")
            raise

    @staticmethod
    def build_url(path):
        """构建完整的URL"""
        return f"{BASE_URL}{path}"

class TestDataBuilder:
    @staticmethod
    def build_enterprise_category_payload(**kwargs):
        """构建企业法规分类测试数据"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        random_suffix = TestUtils.generate_random_string(6)
        default_payload = {
            "tenantId": 9007199254740991,
            "categoryName": f"企业法规_{timestamp}_{random_suffix}",  # 动态生成唯一的类别名称
            "parentId": None,
            "description": "123456",
            "createdAt": "2025-04-27T10:10:23.864Z",
            "updatedAt": "2025-04-27T10:10:23.864Z"
        }
        return {**default_payload, **kwargs}

    @staticmethod
    def build_law_category_payload(**kwargs):
        """构建法律法规类别测试数据"""
        default_payload = {
            "tenantId": 9007199254740991,
            "categoryName": f"law_{TestUtils.generate_random_string()}",
            "description": "测试描述"
        }
        return {**default_payload, **kwargs}
        
    @staticmethod
    def build_compliance_case_payload(**kwargs):
        """构建合规案例测试数据"""
        default_payload = {
            "tenantId": 9007199254740991,
            "caseName": f"case_{TestUtils.generate_random_string()}",
            "caseCode": f"CASE_{TestUtils.generate_random_string(6)}",
            "areaType": "INDUSTRY_REGULATION",
            "caseSource": "INTERNAL",
            "level": "GENERAL",
            "summary": "测试案例摘要",
            "keyword": "测试关键词",
            "backgroundDesc": "测试案例背景描述",
            "occurDate": datetime.now().strftime("%Y-%m-%d"),
            "mediaUrl": "",
            "violation": "测试违规行为",
            "riskAnalysis": "测试风险分析",
            "preventionControl": "测试预防控制措施",
            "learningPoints": "测试学习要点",
            "trainingUrl": "",
            "createdBy": "test_user"
        }
        return {**default_payload, **kwargs} 