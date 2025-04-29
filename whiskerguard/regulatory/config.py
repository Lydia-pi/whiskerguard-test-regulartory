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
BASE_URL = os.getenv("BASE_URL", "http://175.27.251.251:8080")
AUTH_TOKEN = os.getenv("AUTH_TOKEN", "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTc0NTkyMzgzMSwiYXV0aCI6IlJPTEVfQURNSU4gUk9MRV9VU0VSIiwiaWF0IjoxNzQ1ODM3NDMxfQ.k6SQR5-cTgy7A1mecKPymn1fm62Vbului7yacDz_ZgI4EKsx9R58wv6KrDBJMXev2V3I3WfNr_HNzGOd2K5ztA")

# API路径配置
class ApiPaths:
    # 企业内部制度类别
    ENTERPRISE_CATEGORY = {
        "BASE": "/services/whiskerguardregulatoryservice/api/enterprise/categories",
        "CREATE": "/services/whiskerguardregulatoryservice/api/enterprise/categories/create",
        "UPDATE": "/services/whiskerguardregulatoryservice/api/enterprise/categories/{id}",
        "DELETE": "/services/whiskerguardregulatoryservice/api/enterprise/categories/{id}",
        "GET": "/services/whiskerguardregulatoryservice/api/enterprise/categories",
        "GET_BY_ID": "/services/whiskerguardregulatoryservice/api/enterprise/categories/{id}"
    }
    
    # 法律法规类别
    LAW_CATEGORY = {
        "BASE": "/services/whiskerguardregulatoryservice/api/law/categories",
        "CREATE": "/services/whiskerguardregulatoryservice/api/law/categories/create",
        "UPDATE": "/services/whiskerguardregulatoryservice/api/law/categories/{id}",
        "DELETE": "/services/whiskerguardregulatoryservice/api/law/categories/{id}",
        "GET": "/services/whiskerguardregulatoryservice/api/law/categories",
        "GET_BY_ID": "/services/whiskerguardregulatoryservice/api/law/categories/{id}"
    }

# 测试配置
class TestConfig:
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