# 存放前后置fixture相关函数
import time
import pytest
from appium import webdriver
from config import *
from appium.options.android import UiAutomator2Options

from page.page_cart import PageCart
from page.page_home import PageHome
from page.page_mine import PageMine
from page.page_search import PageSearch


@pytest.fixture
def app_driver():
    """app驱动函数"""
    # 前置：创建app驱动对象
    # 配置移动端设备信息
    des_caps = {**DEVICE_CONFIG, **APP_CONFIG}
    # 初始化设备配置信息
    option = UiAutomator2Options().load_capabilities(des_caps)
    # 创建驱动对象
    driver = webdriver.Remote(APPIUM_SERVER, options=option)
    yield driver
    # 后置：退出app
    time.sleep(3)
    driver.quit()


@pytest.fixture(scope="function", autouse=True)
def enter_home(app_driver):
    """进入首页"""
    ph = PageHome(app_driver)
    ph.swipe_guide_images()


@pytest.fixture(scope="function")
def enter_mine(enter_home,app_driver):
    """进入我的页面、点击头像"""
    pm = PageMine(app_driver)
    pm.click_mine_page()
    pm.click_head_img()
    # 返回
    return pm


@pytest.fixture
def app_login(enter_mine):
    """登录"""
    enter_mine.login("13800000003", "123456")


@pytest.fixture
def app_search(app_login,app_driver):
    """搜索"""
    page_search = PageSearch(app_driver)
    # 返回首页
    page_search.click_home_btn()
    # 点击搜索
    page_search.search("华为耳机")


@pytest.fixture
def app_cart(app_search,app_driver):
    """添加购物车"""
    page_cart = PageCart(app_driver)
    # 添加购物车
    page_cart.add_cart()