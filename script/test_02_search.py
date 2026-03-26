from base import log
from page.page_search import PageSearch


class TestSearch:

    def test_01_search_success(self, app_driver):
        # 准备数据
        page_search = PageSearch(app_driver)
        # 调用方法
        page_search.search("华为耳机")
        # 打印结果
        result = page_search.get_search_result()
        log.info(f"搜索结果：{result}")
        # 断言
        assert "华为耳机" in result
