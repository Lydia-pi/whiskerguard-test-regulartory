import pytest
import allure
from ..config import ApiPaths, TestConfig
from ..utils import TestUtils, TestDataBuilder

@allure.feature("法律法规管理服务-企业内部制度类别集成测试")
class TestEnterpriseCategoryIntegration:

    @allure.story("完整的分类管理流程测试")
    def test_complete_category_management_flow(self):
        """测试完整的分类管理流程：创建 -> 查询 -> 更新 -> 删除"""
        
        # 1. 创建分类
        create_payload = TestDataBuilder.build_enterprise_category_payload()
        create_url = TestUtils.build_url(ApiPaths.ENTERPRISE_CATEGORY["CREATE"])
        create_response = TestUtils.make_request("POST", create_url, json=create_payload)
        
        assert create_response.status_code == 201
        category_id = create_response.json()["id"]
        
        # 2. 查询分类列表
        list_url = TestUtils.build_url(ApiPaths.ENTERPRISE_CATEGORY["GET"])
        list_response = TestUtils.make_request("GET", list_url)
        
        assert list_response.status_code == 200
        categories = list_response.json()
        assert isinstance(categories, list)
        assert any(cat["id"] == category_id for cat in categories)
        
        # 3. 查询单个分类
        get_url = TestUtils.build_url(ApiPaths.ENTERPRISE_CATEGORY["GET_BY_ID"].format(id=category_id))
        get_response = TestUtils.make_request("GET", get_url)
        
        assert get_response.status_code == 200
        category = get_response.json()
        assert category["id"] == category_id
        assert category["categoryName"] == create_payload["categoryName"]
        
        # 4. 更新分类
        update_payload = TestDataBuilder.build_enterprise_category_payload(
            categoryName=f"updated_cat_{TestUtils.generate_random_string()}",
            description="集成测试更新描述"
        )
        update_url = TestUtils.build_url(ApiPaths.ENTERPRISE_CATEGORY["UPDATE"].format(id=category_id))
        update_response = TestUtils.make_request("PUT", update_url, json=update_payload)
        
        assert update_response.status_code == 200
        updated_category = update_response.json()
        assert updated_category["id"] == category_id
        assert updated_category["categoryName"] == update_payload["categoryName"]
        assert updated_category["description"] == update_payload["description"]
        
        # 5. 删除分类
        delete_url = TestUtils.build_url(ApiPaths.ENTERPRISE_CATEGORY["DELETE"].format(id=category_id))
        delete_response = TestUtils.make_request("DELETE", delete_url)
        
        assert delete_response.status_code == 204
        
        # 6. 验证删除成功
        verify_url = TestUtils.build_url(ApiPaths.ENTERPRISE_CATEGORY["GET_BY_ID"].format(id=category_id))
        verify_response = TestUtils.make_request("GET", verify_url)
        
        assert verify_response.status_code == 404

    @allure.story("批量操作测试")
    def test_batch_operations(self):
        """测试批量创建和删除分类"""
        
        # 1. 批量创建分类
        category_ids = []
        for _ in range(3):
            create_payload = TestDataBuilder.build_enterprise_category_payload()
            create_url = TestUtils.build_url(ApiPaths.ENTERPRISE_CATEGORY["CREATE"])
            create_response = TestUtils.make_request("POST", create_url, json=create_payload)
            
            assert create_response.status_code == 201
            category_ids.append(create_response.json()["id"])
        
        # 2. 验证所有分类都已创建
        list_url = TestUtils.build_url(ApiPaths.ENTERPRISE_CATEGORY["GET"])
        list_response = TestUtils.make_request("GET", list_url)
        
        assert list_response.status_code == 200
        categories = list_response.json()
        for category_id in category_ids:
            assert any(cat["id"] == category_id for cat in categories)
        
        # 3. 批量删除分类
        for category_id in category_ids:
            delete_url = TestUtils.build_url(ApiPaths.ENTERPRISE_CATEGORY["DELETE"].format(id=category_id))
            delete_response = TestUtils.make_request("DELETE", delete_url)
            assert delete_response.status_code == 204
        
        # 4. 验证所有分类都已删除
        for category_id in category_ids:
            verify_url = TestUtils.build_url(ApiPaths.ENTERPRISE_CATEGORY["GET_BY_ID"].format(id=category_id))
            verify_response = TestUtils.make_request("GET", verify_url)
            assert verify_response.status_code == 404 