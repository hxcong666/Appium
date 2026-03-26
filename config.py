import os

# 项目基础路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Appium服务配置
APPIUM_SERVER = "http://127.0.0.1:4723/wd/hub"

# 设备配置
DEVICE_CONFIG = {
    "platformName": "Android",
    "platformVersion": "12",
    "deviceName": "mumu"
}

# 应用配置
APP_CONFIG = {
    "appPackage": "com.tpshop.malls",
    "appActivity": ".SplashActivity"
}

# 等待时间配置
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 15




