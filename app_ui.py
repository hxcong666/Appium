from appium import webdriver
import time

from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

# 1. 配置连接参数（Capabilities）
capabilities = {
    "deviceName": "emulator-5554",
    "platformName": "Android",
    "platformVersion": "9",
    "automationName": "UiAutomator2",
    # "app": "D:\\AppProject1\\tpshopAPP.apk"
}

# 创建Appium Server选项
appium_options = UiAutomator2Options()
appium_options.load_capabilities(capabilities)

# 2. 创建与 Appium 服务的连接
driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4723/wd/hub',
    options=appium_options
)


# driver.install_app("tpshopAPP.apk")
#查看是否有tpshopAPP.


print(driver.is_app_installed("com.tpshop.malls"))




# # 设置隐式等待时间为 5 秒
# driver.implicitly_wait(5)
# driver.find_element(by=AppiumBy.XPATH, value="//*[@text='蓝牙']").click()
# time.sleep(2)
# driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageView[@resource-id='android:id/icon'][1]").click()
# # 3. 测试：等待3秒后关闭连接
time.sleep(3)
driver.quit()