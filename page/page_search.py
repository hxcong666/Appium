from selenium.webdriver.common.by import By

from base.page_base import PageBase


class PageSearch(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        # 元素定位器
        self.home_btn = (By.ID, "com.tpshop.malls:id/home_ll")
        self.default_search_btn = (By.ID, "com.tpshop.malls:id/default_search_et")
        self.search_text = (By.ID, "com.tpshop.malls:id/search_et")
        self.search_btn = (By.ID, "com.tpshop.malls:id/search_btn")
        # 搜索结果：商品名
        self.result_text = (By.ID, "com.tpshop.malls:id/product_name_tv")

    def click_home_btn(self):
        """进入首页"""
        self.base_click(self.home_btn)

    def click_default_search(self):
        """默认搜索框"""
        self.base_click(self.default_search_btn)

    def input_search_text(self, text):
        """搜索关键词"""
        self.base_input_text(self.search_text, text)

    def click_search_btn(self):
        """搜索按钮"""
        self.base_click(self.search_btn)

    def search(self, text):
        """搜索方法"""
        self.click_default_search()
        self.input_search_text(text)
        self.click_search_btn()

    def get_search_result(self):
        """获取搜索结果"""
        return self.base_get_text(self.result_text)
