import pytest
import requests
import allure

BASE_URL = "http://175.27.251.251:8080"
# 直接把你的 Bearer Token 写在这里
AUTH_HEADER = {
    "Content-Type": "application/json",
    "Authorization": "kwNiwiYXV0aCI6IlJPTEVfQURNSU4gUk9MRV9VU0VSIiwiaWF0IjoxNzQ0MzUxOTA2fQ.fosoVYzk-N7inGu_RaWHHKbxoQjsrd5fRIqbQgcfI5lY1w4RPtSL3WUN66LGTb7GAY4FWso2CfEZIWNUCEamgABearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTc0NTkyMzgzMSwiYXV0aCI6IlJPTEVfQURNSU4gUk9MRV9VU0VSIiwiaWF0IjoxNzQ1ODM3NDMxfQ.k6SQR5-cTgy7A1mecKPymn1fm62Vbului7yacDz_ZgI4EKsx9R58wv6KrDBJMXev2V3I3WfNr_HNzGOd2K5ztA"
}

@allure.feature("法律法规管理服务-企业内部制度类别")
class TestEnterpriseCategory:

    @allure.story("添加企业内部法规分类")
    @pytest.mark.parametrize("payload, expected_code", [
        (
            {
                "tenantId": 9007199254740991,
                "categoryName": "法规01",
                "parentId": None,
                "description": "法规01",
                "createdAt": "2025-04-27T10:10:23.864Z",
                "updatedAt": "2025-04-27T10:10:23.864Z"
            },
            201
        )
    ])
    def test_add_enterprise_category(self, payload, expected_code):
        url = f"{BASE_URL}/services/whiskerguardregulatoryservice/api/enterprise/categories/create"
        response = requests.post(url, json=payload, headers=AUTH_HEADER)

        # 调试输出
        print("▶▶▶ URL:", url)
        print("▶▶▶ 返回码:", response.status_code)
        print("▶▶▶ 返回体:", response.text[:201])

        # 断言
        assert response.status_code == expected_code
        # 如需断言业务字段可加上
        # data = response.json()
        # assert data.get("code") == 0
