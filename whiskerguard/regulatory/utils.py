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
            response = requests.request(
                method=method,
                url=url,
                headers=COMMON_HEADERS,
                **kwargs
            )
            logging.info(f"Request: {method} {url}")
            logging.info(f"Response Status: {response.status_code}")
            logging.info(f"Response Body: {response.text}")
            return response
        except requests.RequestException as e:
            logging.error(f"Request failed: {str(e)}")
            raise

    @staticmethod
    def build_url(path):
        """构建完整的URL"""
        return f"{BASE_URL}{path}"

class TestDataBuilder:
    @staticmethod
    def build_enterprise_category_payload(**kwargs):
        """构建企业内部制度类别测试数据"""
        default_payload = {
            "tenantId": 9007199254740991,
            "categoryName": f"cat_{TestUtils.generate_random_string()}",
            "description": "测试描述"
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