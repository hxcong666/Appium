from base import log
from page.page_cart import PageCart


class TestCart:

    def test_01_add_cart_success(self,app_driver,app_search):
        # 准备数据
        page_cart = PageCart(app_driver)
        # 调用方法
        page_cart.add_cart()
        # 打印日志
        result = page_cart.get_product_name()
        log.info(f"添加购物车：{result}")
        # 断言
        assert "华为耳机" in result