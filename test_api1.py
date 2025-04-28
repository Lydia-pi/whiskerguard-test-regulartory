# 你是资深测试工程师，下面是 Postman Collection 文件路径 "apifox_collection.json"，请帮我：
# 1. 将其中的每个接口自动转换为 Pytest + Requests 的测试函数。
# 2. 每个测试函数以 test_<接口名> 命名，并断言 HTTP 状态码和 JSON 关键字段。
# 3. 报告输出格式为 Allure 友好（使用 @allure.feature 和 @allure.story 装饰）。

import pytest
import requests
import allure

BASE_URL = "http://192.168.1.46:8080/services"  # 本地实际 baseUrl

@allure.feature("法律法规管理服务-企业内部制度类别")
class TestEnterpriseCategory:
    @allure.story("添加企业内部法规分类")
    @pytest.mark.parametrize("payload, expected_code", [
        ({
            "tenantId": 9007199254740991,
            "categoryName": "123456",
            "parentId": None,
            "description": "123456",
            "createdAt": "2025-04-27T10:10:23.864Z",
            "updatedAt": "2025-04-27T10:10:23.864Z"
        }, 200)
    ])
    def test_add_enterprise_category(self, payload, expected_code):
        url = f"{BASE_URL}/whiskerguardregulatoryservice/api/enterprise/categories/create"
        with allure.step("发送添加企业内部法规分类请求"):
            response = requests.post(url, json=payload)
        with allure.step("断言响应状态码和返回字段"):
            assert response.status_code == expected_code
            json_data = response.json()
            assert "code" in json_data



    @allure.story("更新企业内部法规分类")
    @pytest.mark.parametrize("category_id, payload, expected_code", [
        (
            9007199254740991,
            {
                "id": 9007199254740991,
                "categoryName": "string",
                "parentId": 9007199254740991,
                "description": "string",
                "createdAt": "2025-04-27T10:28:48.875Z",
                "updatedAt": "2025-04-27T10:28:48.875Z",
                "children": ["string"]
            },
            200
        )
    ])
    def test_update_enterprise_category(self, category_id, payload, expected_code):
        url = f"{BASE_URL}/whiskerguardregulatoryservice/api/enterprise/categories/update/{category_id}"
        with allure.step("发送更新企业内部法规分类请求"):
            response = requests.post(url, json=payload)
        with allure.step("断言响应状态码和返回字段"):
            assert response.status_code == expected_code
            json_data = response.json()
            assert "code" in json_data


    @allure.story("部分更新企业内部法规分类")
    @pytest.mark.parametrize("category_id, payload, expected_code", [
        (
            9007199254740991,
            {
                "id": 9007199254740991,
                "categoryName": "string",
                "parentId": 9007199254740991,
                "description": "string",
                "createdAt": "2025-04-27T10:27:54.476Z",
                "updatedAt": "2025-04-27T10:27:54.476Z",
                "children": ["string"]
            },
            200
        )
    ])
    def test_partial_update_enterprise_category(self, category_id, payload, expected_code):
        url = f"{BASE_URL}/whiskerguardregulatoryservice/api/enterprise/categories/partialUpdate/{category_id}"
        with allure.step("发送部分更新企业内部法规分类请求"):
            response = requests.post(url, json=payload)
        with allure.step("断言响应状态码和返回字段"):
            assert response.status_code == expected_code
            json_data = response.json()
            assert "code" in json_data

    @allure.story("获取指定租户分类的树形结构")
    @pytest.mark.parametrize("params, expected_code, expected_keys", [
        (
            {"tenantId": 9007199254740991},
            200,
            [
                {
                    "id": 9007199254740991,
                    "categoryName": "string",
                    "parentId": 9007199254740991,
                    "description": "string",
                    "createdAt": "2025-04-27T10:30:30.856Z",
                    "updatedAt": "2025-04-27T10:30:30.856Z",
                    "children": ["string"]
                }
            ]
        )
    ])
    def test_get_category_tree(self, params, expected_code, expected_keys):
        url = f"{BASE_URL}/whiskerguardregulatoryservice/api/enterprise/categories/tree"
        with allure.step("发送获取分类树形结构请求"):
            response = requests.get(url, params=params)
        with allure.step("断言响应状态码和返回字段"):
            assert response.status_code == expected_code
            json_data = response.json()
            assert "data" in json_data
            # 可选：校验返回结构
            # assert json_data["data"] == expected_keys

    @allure.story("根据分类id查询指定的分类")
    @pytest.mark.parametrize("category_id, expected_code", [("test_id", 200)])
    def test_get_category_by_id(self, category_id, expected_code):
        url = f"{BASE_URL}/whiskerguardregulatoryservice/api/enterprise/categories/get/{category_id}"
        with allure.step("发送根据ID查询分类请求"):
            response = requests.get(url)
        with allure.step("断言响应状态码和返回字段"):
            assert response.status_code == expected_code
            json_data = response.json()
            assert "data" in json_data

    @allure.story("删除分类")
    @pytest.mark.parametrize("category_id, expected_code", [("test_id", 200)])
    def test_delete_category(self, category_id, expected_code):
        url = f"{BASE_URL}/whiskerguardregulatoryservice/api/enterprise/categories/delete/{category_id}"
        with allure.step("发送删除分类请求"):
            response = requests.get(url)
        with allure.step("断言响应状态码和返回字段"):
            assert response.status_code == expected_code
            json_data = response.json()
            assert "code" in json_data

# ... 省略后续接口，建议分批生成，避免单文件过大 ...