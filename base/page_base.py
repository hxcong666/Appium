from appium.webdriver.common.appiumby import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from script import log
from config import EXPLICIT_WAIT


class PageBase:
    def __init__(self, driver):
        self.driver = driver

    def fd_element(self, locator, timeout=EXPLICIT_WAIT):
        """定位单个元素（带显式等待）"""
        try:
            log.info(f"定位元素: {locator}")
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator))
        except Exception as e:
            log.error(f"元素定位失败: {locator} - {str(e)}")
            raise

    def fd_elements(self, locator, timeout=EXPLICIT_WAIT):
        """定位多个元素（带显式等待）"""
        try:
            log.info(f"定位多个元素: {locator}")
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator))
        except Exception as e:
            log.error(f"元素组定位失败: {locator} - {str(e)}")
            raise

    def base_click(self, locator):
        """点击元素"""
        log.info(f"点击元素: {locator}")
        self.fd_element(locator).click()

    def base_input_text(self, locator, text):
        """输入文本"""
        log.info(f"在元素 {locator} 输入文本: {text}")
        element = self.fd_element(locator)
        element.clear()
        element.send_keys(text)

    def base_get_text(self, locator):
        """获取元素文本"""
        text = self.fd_element(locator).text
        log.info(f"获取元素文本: {locator} -> {text}")
        return text

    def base_swipe(self, start_x, start_y, end_x, end_y, duration=10):
        """滑动操作"""
        log.info(f"滑动操作: ({start_x},{start_y}) -> ({end_x},{end_y})")
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def base_get_toast(self,toast_loc, timeout=10):
        """获取Toast提示文本"""
        try:
            # toast_loc = (By.XPATH, '//android.widget.Toast[1]')
            toast = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(toast_loc))
            text = toast.text
            log.info(f"获取Toast提示: {text}")
            return text
        except Exception as e:
            log.error(f"获取Toast失败: {str(e)}")
            return ""

