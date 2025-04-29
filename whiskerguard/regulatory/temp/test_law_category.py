import pytest
import requests
import allure

BASE_URL = "http://127.0.0.1"  # 请替换为实际 baseUrl

@allure.feature("法律法规管理服务-法律法规分类管理")
class TestLawCategory:
    @allure.story("创建法律法规分类")
    @pytest.mark.parametrize("payload, expected_code", [({}, 200)])
    def test_create_law_category(self, payload, expected_code):
        url = f"{BASE_URL}/whiskerguardregulatoryservice/api/laws/categories/create"
        with allure.step("发送创建法律法规分类请求"):
            response = requests.post(url, json=payload)
        with allure.step("断言响应状态码和返回字段"):
            assert response.status_code == expected_code
            assert "code" in response.json()

    @allure.story("更新现有法律法规分类")
    @pytest.mark.parametrize("category_id, payload, expected_code", [("test_id", {}, 200)])
    def test_update_law_category(self, category_id, payload, expected_code):
        url = f"{BASE_URL}/whiskerguardregulatoryservice/api/laws/categories/update/{category_id}"
        with allure.step("发送更新法律法规分类请求"):
            response = requests.post(url, json=payload)
        with allure.step("断言响应状态码和返回字段"):
            assert response.status_code == expected_code
            assert "code" in response.json()

    @allure.story("部分更新现有法律法规分类")
    @pytest.mark.parametrize("category_id, payload, expected_code", [("test_id", {}, 200)])
    def test_partial_update_law_category(self, category_id, payload, expected_code):
        url = f"{BASE_URL}/whiskerguardregulatoryservice/api/laws/categories/partialUpdate/{category_id}"
        with allure.step("发送部分更新法律法规分类请求"):
            response = requests.post(url, json=payload)
        with allure.step("断言响应状态码和返回字段"):
            assert response.status_code == expected_code
            assert "code" in response.json()

    @allure.story("获取所有法律法规分类（分页）")
    @pytest.mark.parametrize("params, expected_code", [({}, 200)])
    def test_get_law_categories_page(self, params, expected_code):
        url = f"{BASE_URL}/whiskerguardregulatoryservice/api/laws/categories/page"
        with allure.step("发送获取所有法律法规分类（分页）请求"):
            response = requests.get(url, params=params)
        with allure.step("断言响应状态码和返回字段"):
            assert response.status_code == expected_code
            assert "data" in response.json()

    @allure.story("获取指定ID的法律法规分类")
    @pytest.mark.parametrize("category_id, expected_code", [("test_id", 200)])
    def test_get_law_category_by_id(self, category_id, expected_code):
        url = f"{BASE_URL}/whiskerguardregulatoryservice/api/laws/categories/get/{category_id}"
        with allure.step("发送获取指定ID的法律法规分类请求"):
            response = requests.get(url)
        with allure.step("断言响应状态码和返回字段"):
            assert response.status_code == expected_code
            assert "data" in response.json()

    @allure.story("删除指定ID的法律法规分类")
    @pytest.mark.parametrize("category_id, expected_code", [("test_id", 200)])
    def test_delete_law_category(self, category_id, expected_code):
        url = f"{BASE_URL}/whiskerguardregulatoryservice/api/laws/categories/delete/{category_id}"
        with allure.step("发送删除指定ID的法律法规分类请求"):
            response = requests.get(url)
        with allure.step("断言响应状态码和返回字段"):
            assert response.status_code == expected_code
            assert "code" in response.json()

    @allure.story("获取法律法规分类的树形结构")
    @pytest.mark.parametrize("params, expected_code", [({}, 200)])
    def test_get_law_category_tree(self, params, expected_code):
        url = f"{BASE_URL}/whiskerguardregulatoryservice/api/laws/categories/tree"
        with allure.step("发送获取法律法规分类树形结构请求"):
            response = requests.get(url, params=params)
        with allure.step("断言响应状态码和返回字段"):
            assert response.status_code == expected_code
            assert "data" in response.json() 