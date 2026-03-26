# 导包
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import By

# 配置移动端设备信息
des_caps = {
    "platformName": "Android",  # 移动端系统平台
    "platformVersion": "12",  # 平台对应版本
    "deviceName": "mumu",  # 设备名称（可以随便写）
    "appPackage": "com.tpshop.malls",  # 包名
    "appActivity": ".SplashActivity"  # Activity页面名
}
# 初始化设备配置信息
option = UiAutomator2Options().load_capabilities(des_caps)
# 创建驱动对象
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=option)
# APP操作
time.sleep(4)
# 1.滑动图片进入首页
for i in range(3):
    driver.swipe(1000, 900, 100, 900)
# 等待3秒进入首页
time.sleep(3)


# 暂停3秒
time.sleep(3)
# 关闭驱动
driver.quit()
