

from app_ui import driver
from page.page_home import PageHome


class TestHome:
    # 前置操作
    def setup(self):
        """每个测试用例执行前的准备工作"""
        self.driver = driver
        self.home_page = PageHome(self.driver)

    def teardown(self):
        """每个测试用例执行后的清理工作"""
        self.driver.quit()

    def arive(self):
        self.home_page.swipe_guide_images()