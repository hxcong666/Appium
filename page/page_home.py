from appium.webdriver.common.appiumby import By

from base import log
from base.page_base import PageBase


class PageHome(PageBase):

    def __init__(self, driver):
        super().__init__(driver)

    def swipe_guide_images(self, count=3):
        """滑动引导页图片"""
        log.info(f"滑动引导页 {count} 次")
        for _ in range(count):
            self.base_swipe(1000, 900, 100, 900)
        return self
