# 导包
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By

# 配置移动端设备信息
des_caps = {
    "platformName": "Android",  # 移动端系统平台
    "platformVersion": "12",  # 平台对应版本
    "deviceName": "mumu",  # 设备名称（可以随便写）
    # "appPackage": "com.tpshop.malls",  # 包名
    # "appActivity": ".SplashActivity"  # Activity页面名
}
# 初始化设备配置信息
option = UiAutomator2Options().load_capabilities(des_caps)
# 创建驱动对象
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=option)
# 获取app包名和Activity名
# print(driver.current_package)
# print(driver.current_activity)
# 判断app是否安装
print(driver.is_app_installed("com.tpshop.malls"))
# driver.install_app(r"E:\00A-AI测试\02-AI测试-自动化测试\code\appProject1\tpshopAPP.apk")
# driver.remove_app("com.tpshop.malls")
# 暂停3秒
time.sleep(3)
# 关闭驱动
driver.quit()
