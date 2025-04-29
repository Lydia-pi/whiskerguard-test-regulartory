from locust import HttpUser, task, between
from whiskerguard.regulatory.config import ApiPaths, TestConfig, COMMON_HEADERS
from whiskerguard.regulatory.utils import TestDataBuilder

class EnterpriseCategoryUser(HttpUser):
    """企业内部制度类别性能测试类"""
    wait_time = between(TestConfig.PERFORMANCE["THINK_TIME"], TestConfig.PERFORMANCE["THINK_TIME"] * 2)
    
    def on_start(self):
        """用户启动时的初始化操作"""
        self.headers = COMMON_HEADERS

    @task(1)
    def get_categories(self):
        """获取分类列表"""
        self.client.get(
            ApiPaths.ENTERPRISE_CATEGORY["GET"],
            headers=self.headers,
            name="获取分类列表"
        )

    @task(2)
    def create_category(self):
        """创建分类"""
        payload = TestDataBuilder.build_enterprise_category_payload()
        self.client.post(
            ApiPaths.ENTERPRISE_CATEGORY["CREATE"],
            json=payload,
            headers=self.headers,
            name="创建分类"
        )

    @task(1)
    def update_category(self):
        """更新分类"""
        # 先创建一个分类
        create_payload = TestDataBuilder.build_enterprise_category_payload()
        create_response = self.client.post(
            ApiPaths.ENTERPRISE_CATEGORY["CREATE"],
            json=create_payload,
            headers=self.headers,
            name="创建分类(更新前)"
        )
        
        if create_response.status_code == 201:
            category_id = create_response.json()["id"]
            update_payload = TestDataBuilder.build_enterprise_category_payload(
                categoryName=f"updated_cat_{TestDataBuilder.generate_random_string()}"
            )
            self.client.put(
                ApiPaths.ENTERPRISE_CATEGORY["UPDATE"].format(id=category_id),
                json=update_payload,
                headers=self.headers,
                name="更新分类"
            )

    @task(1)
    def delete_category(self):
        """删除分类"""
        # 先创建一个分类
        create_payload = TestDataBuilder.build_enterprise_category_payload()
        create_response = self.client.post(
            ApiPaths.ENTERPRISE_CATEGORY["CREATE"],
            json=create_payload,
            headers=self.headers,
            name="创建分类(删除前)"
        )
        
        if create_response.status_code == 201:
            category_id = create_response.json()["id"]
            self.client.delete(
                ApiPaths.ENTERPRISE_CATEGORY["DELETE"].format(id=category_id),
                headers=self.headers,
                name="删除分类"
            ) 