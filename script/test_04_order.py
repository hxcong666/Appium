import pytest
from base import log
from page.page_order import PageOrder


class TestOrder:

    # 自定义mark标签，筛选冒烟测试的用例
    @pytest.mark.smoke
    def test_01_order_success(self, app_driver, app_login, app_search, app_cart):
        """下单成功"""
        page_order = PageOrder(app_driver)
        page_order.order_settlement()  # 结算
        page_order.order_pay()  # 支付
        result = page_order.get_order_success()
        log.info(f"下单结果：{result}")
        assert '确认订单成功' == result
