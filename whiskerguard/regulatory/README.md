# 法规管理服务测试框架

## 目录结构

```
regulatory/
├── config.py                 # 配置文件
├── utils.py                  # 工具类
├── requirements.txt          # 依赖管理
├── unit/                    # 单元测试
│   └── test_enterprise_category.py
├── performance/             # 性能测试
│   └── test_enterprise_category_perf.py
├── stress/                  # 压力测试
│   └── test_enterprise_category_stress.py
└── integration/             # 集成测试
    └── test_enterprise_category_integration.py
```

## 环境要求

- Python 3.8+
- pip

## 安装依赖

```bash
pip install -r requirements.txt
```

## 测试类型说明

### 1. 单元测试

运行所有单元测试：
```bash
pytest test_*.py -v
```

生成 Allure 报告：
```bash
pytest test_*.py --alluredir=./allure-results
allure serve ./allure-results
```

### 2. 性能测试

使用 Locust 运行性能测试：
```bash
locust -f performance/test_enterprise_category_perf.py --host=http://your-api-host
```

### 3. 压力测试

使用 Locust 运行压力测试：
```bash
locust -f stress/test_enterprise_category_stress.py --host=http://your-api-host
```

### 4. 集成测试

运行集成测试：
```bash
pytest integration/test_*.py -v
```

## 配置说明

### 环境变量

- `ENV`: 环境选择（dev/test/prod）
- `BASE_URL`: API 基础地址
- `AUTH_TOKEN`: 认证令牌

### 测试配置

在 `config.py` 中可以配置：
- API 路径
- 性能测试参数
- 压力测试参数
- 集成测试参数
- 日志配置

## 工具类说明

### TestUtils

- `generate_random_string()`: 生成随机字符串
- `get_current_timestamp()`: 获取当前时间戳
- `make_request()`: 统一的请求处理方法
- `build_url()`: 构建完整的 URL

### TestDataBuilder

- `build_enterprise_category_payload()`: 构建企业内部制度类别测试数据
- `build_law_category_payload()`: 构建法律法规类别测试数据

## 最佳实践

1. 测试用例命名规范：
   - 单元测试：`test_*.py`
   - 性能测试：`*_perf.py`
   - 压力测试：`*_stress.py`
   - 集成测试：`*_integration.py`

2. 测试数据管理：
   - 使用 TestDataBuilder 构建测试数据
   - 避免硬编码测试数据
   - 使用随机数据避免冲突

3. 错误处理：
   - 使用 try-except 捕获异常
   - 记录详细的错误日志
   - 提供清晰的错误信息

4. 测试报告：
   - 使用 Allure 生成测试报告
   - 添加详细的测试步骤说明
   - 包含测试数据和结果

## 注意事项

1. 运行测试前确保：
   - 环境变量已正确配置
   - 依赖包已安装
   - 测试环境可访问

2. 性能测试注意事项：
   - 选择合适的并发用户数
   - 设置合理的思考时间
   - 监控系统资源使用

3. 压力测试注意事项：
   - 逐步增加负载
   - 监控系统响应时间
   - 注意数据清理

4. 集成测试注意事项：
   - 测试数据隔离
   - 测试用例独立性
   - 完整的业务流程覆盖 