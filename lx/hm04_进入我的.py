# 导包
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
# 2.点击我的
# driver.find_element(By.ID, "com.tpshop.malls:id/mine_ll").click()
ele1 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "com.tpshop.malls:id/mine_ll")))
ele1.click()
# 3.点击头像
ele2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "com.tpshop.malls:id/head_img")))
ele2.click()
# 4.输入登录信息
# 用户名
ele3 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@text='请输入账号']")))
ele3.send_keys("13800000001")
ele4 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@text='请输入密码']")))
ele4.send_keys("123456")
ele5 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "com.tpshop.malls:id/agree_btn")))
ele5.click()
ele6 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "com.tpshop.malls:id/login_tv")))
ele6.click()
# 通过toast提示断言
ele7 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Toast[@text="登录成功"]')))
res = ele7.text
print(res)
assert "登录成功" in res
# 断言
# ele7 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "com.tpshop.malls:id/nick_name_tv")))
# result = ele7.text
# assert "13800000001" in result
# 暂停3秒
time.sleep(3)
# 关闭驱动
driver.quit()
