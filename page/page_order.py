from selenium.webdriver.common.by import By
from base.page_base import PageBase


class PageOrder(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        # 下单页面相关元素定位
        # __buy_btn（双下划线开头）：私有属性
        # 只能在类内部访问
        # 外部无法直接访问（会触发名称改写机制）

        # _buy_btn（单下划线开头）：受保护属性
        # 约定俗成表示应该在子类或内部使用
        # 但实际上仍可被外部访问

        # buy_btn（无下划线）：公有属性
        # 可以随意访问
        self.__buy_btn = By.ID, "com.tpshop.malls:id/buy_tv"
        self.__submit_btn = By.ID, "com.tpshop.malls:id/submit_tv"
        self.__pay_btn = (By.ID, 'com.tpshop.malls:id/pay_btn')
        self.__pwd_input = (By.ID, 'com.tpshop.malls:id/pwd_et')
        self.__sure_btn = (By.ID, 'com.tpshop.malls:id/sure_tv')
        self.__order_success = (By.ID, 'com.tpshop.malls:id/title_tv')

    def click_buy_btn(self):
        """立即购买"""
        self.base_click(self.__buy_btn)

    def click_submit_btn(self):
        """提交订单"""
        self.base_click(self.__submit_btn)

    def click_pay_btn(self):
        """立即支付"""
        self.base_click(self.__pay_btn)

    def input_pwd(self, pwd):
        """输入密码"""
        self.base_input_text(self.__pwd_input, pwd)

    def click_sure_btn(self):
        """点击确定"""
        self.base_click(self.__sure_btn)

    def get_order_success(self):
        """获取订单成功"""
        return self.base_get_text(self.__order_success)

    def order_settlement(self):
        """订单结算"""
        self.click_buy_btn() # 点击结算按钮
        self.click_submit_btn() # 点击提交按钮

    def order_pay(self,pwd='123456'):
        """订单支付"""
        self.click_pay_btn()  # 点击支付按钮
        self.input_pwd(pwd)  # 输入密码
        self.click_sure_btn()  # 点击确定


