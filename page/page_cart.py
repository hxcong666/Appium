import time

from selenium.webdriver.common.by import By
from base.page_base import PageBase


class PageCart(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        # 元素定位器
        self.__product_img = By.ID,"com.tpshop.malls:id/product_pic_img"
        self.__add_btn = By.ID,"com.tpshop.malls:id/add_cart_tv"
        self.__confirm_btn = By.ID,"com.tpshop.malls:id/confirm_tv"
        self.__icon_img = By.ID,"com.tpshop.malls:id/bottom_cart_img"
        # 添加结果：商品名称
        self.__product_name = By.ID, "com.tpshop.malls:id/product_name_tv"

    def click_product_img(self):
        """点击商品图片"""
        self.base_click(self.__product_img)

    def click_add_btn(self):
        """点击添加按钮"""
        self.base_click(self.__add_btn)

    def click_confirm_btn(self):
        """点击确认按钮"""
        self.base_click(self.__confirm_btn)

    def click_icon_img(self):
        """点击图标"""
        self.base_click(self.__icon_img)
        time.sleep(1)

    def add_cart(self):
        """业务：添加购物车"""
        self.click_product_img()
        self.click_add_btn()
        self.click_confirm_btn()
        self.click_icon_img()

    def get_product_name(self):
        """获取商品名称"""
        return self.base_get_text(self.__product_name)
