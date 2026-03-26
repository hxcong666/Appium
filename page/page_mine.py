from appium.webdriver.common.appiumby import By
from base.page_base import PageBase


class PageMine(PageBase):
    # 元素定位器：进入我的
    MINE_BTN = (By.ID, "com.tpshop.malls:id/mine_ll")
    HEAD_IMG = (By.ID, "com.tpshop.malls:id/head_img")
    GUIDE_IMAGE = (By.ID, "com.tpshop.malls:id/guide_image")
    # 元素定位器：登录页
    USERNAME_INPUT = (By.XPATH, "//*[@text='请输入账号']")
    PASSWORD_INPUT = (By.XPATH, "//*[@text='请输入密码']")
    AGREE_BTN = (By.ID, "com.tpshop.malls:id/agree_btn")
    LOGIN_BTN = (By.ID, "com.tpshop.malls:id/login_tv")
    LOGIN_SUCCESS_TOAST = (By.XPATH, '//android.widget.Toast[@text="登录成功"]')

    def __init__(self, driver):
        super().__init__(driver)

    def enter_mine_page(self):
        """进入'我的'页面"""
        self.base_click(self.MINE_BTN)

    def click_head_img(self):
        """点击头像"""
        self.base_click(self.HEAD_IMG)

    def input_username(self, username):
        """输入用户名"""
        self.base_input_text(self.USERNAME_INPUT, username)

    def input_password(self, password):
        """输入密码"""
        self.base_input_text(self.PASSWORD_INPUT, password)

    def click_agree(self):
        """点击同意协议"""
        self.base_click(self.AGREE_BTN)

    def click_login(self):
        """点击登录按钮"""
        self.base_click(self.LOGIN_BTN)

    def login(self, username, password):
        """执行登录操作"""
        # 使用默认测试数据
        self.input_username(username)
        self.input_password(password)
        self.click_agree()
        self.click_login()

    def get_login_result(self):
        """获取登录结果Toast"""
        return self.base_get_toast(self.LOGIN_SUCCESS_TOAST)




