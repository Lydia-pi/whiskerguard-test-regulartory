import os
from datetime import datetime

# 环境配置
class Environment:
    DEV = "dev"
    TEST = "test"
    PROD = "prod"

# 当前环境
CURRENT_ENV = os.getenv("ENV", Environment.DEV)

# API基础配置
BASE_URL = os.getenv("BASE_URL", "http://175.27.251.251:8080/services/whiskerguardregulatoryservice")
AUTH_TOKEN = "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTc0NjAwMzUxOCwiYXV0aCI6IlJPTEVfQURNSU4gUk9MRV9VU0VSIiwiaWF0IjoxNzQ1OTE3MTE4fQ.3G3KYqJRMQZEqHzC1RKeodwahhm8VuDAQevBAIzkGb6SQTqyQ6BQRy_aJIyV6dA5-JaCfNDxbxGxc-PUeJRG8g"

# API路径配置
class ApiPaths:
    """API路径配置"""
    ENTERPRISE_CATEGORY = {
        'BASE': '/api/enterprise/categories',
        'CREATE': '/api/enterprise/categories/create',
        'UPDATE': '/api/enterprise/categories/update/{id}',
        'PARTIAL_UPDATE': '/api/enterprise/categories/partialUpdate/{id}',
        'DELETE': '/api/enterprise/categories/delete/{id}',
        'GET_BY_ID': '/api/enterprise/categories/get/{id}',
        'PAGE': '/api/enterprise/categories/page',
        'TREE': '/api/enterprise/categories/tree'
    }
    
    LAW_CATEGORY = {
        'BASE': '/api/laws/categories',
        'CREATE': '/api/laws/categories/create',
        'UPDATE': '/api/laws/categories/update/{id}',
        'PARTIAL_UPDATE': '/api/laws/categories/partialUpdate/{id}',
        'DELETE': '/api/laws/categories/delete/{id}',
        'GET_BY_ID': '/api/laws/categories/get/{id}',
        'PAGE': '/api/laws/categories/page',
        'TREE': '/api/laws/categories/tree'
    }
    
    COMPLIANCE_CASE = {
        'BASE': '/api/compliance/cases',
        'CREATE': '/api/compliance/cases/create',
        'UPDATE': '/api/compliance/cases/update/{id}',
        'DELETE': '/api/compliance/cases/{id}',
        'GET_BY_ID': '/api/compliance/cases/{id}',
        'PAGE': '/api/compliance/cases/page'
    }

# 测试配置
class TestConfig:
    # API基础配置
    BASE_URL = "http://175.27.251.251:8080/services/whiskerguardregulatoryservice"
    AUTH_TOKEN = "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTc0NjAwMzUxOCwiYXV0aCI6IlJPTEVfQURNSU4gUk9MRV9VU0VSIiwiaWF0IjoxNzQ1OTE3MTE4fQ.3G3KYqJRMQZEqHzC1RKeodwahhm8VuDAQevBAIzkGb6SQTqyQ6BQRy_aJIyV6dA5-JaCfNDxbxGxc-PUeJRG8g"
    HEADERS = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AUTH_TOKEN}"
    }
    
    # 性能测试配置
    PERFORMANCE = {
        "THREADS": 10,
        "RAMP_UP": 5,
        "DURATION": 300,
        "THINK_TIME": 1
    }
    
    # 压力测试配置
    STRESS = {
        "THREADS": 50,
        "RAMP_UP": 10,
        "DURATION": 600,
        "THINK_TIME": 0.5
    }
    
    # 集成测试配置
    INTEGRATION = {
        "TIMEOUT": 30,
        "RETRY_COUNT": 3,
        "RETRY_DELAY": 1
    }

# 通用请求头
COMMON_HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {AUTH_TOKEN}"
}

# 日志配置
class LogConfig:
    LEVEL = "INFO"
    FORMAT = '%(asctime)s %(levelname)s %(message)s'
    FILE = f"logs/regulatory_{datetime.now().strftime('%Y%m%d')}.log" 