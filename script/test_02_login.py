from page.page_home import PageHome
from script import log
from page.page_mine import PageMine

from tools import DriverTools
class TestMine:
    # 前置操作
    def setup_method(self):
        """每个测试用例执行前的准备工作"""
        self.driver = DriverTools.get_app_driver()
        self.home_page = PageHome(self.driver)
        self.mine_page = PageMine(self.driver)
        #滑动到首页
        self.home_page.swipe_guide_images()
        # 进入我的页面
        self.mine_page.enter_mine_page()
        # 点击头像进入登录页
        self.mine_page.click_head_img()

    def teardown_method(self):
        """每个测试用例执行后的清理工作"""
        DriverTools.quit_app_driver()


    def test_login_success(self):
        """测试登录成功场景"""

        # 执行登录操作
        self.mine_page.login("testuser", "testpass")
        # 获取登录结果
        result = self.mine_page.get_login_result()
        log.info(f"登录结果: {result}")
        # 断言登录成功
        assert "登录成功" in result

    def test_login_with_empty_username(self):
        """测试用户名为空的登录场景"""

        # 只输入密码，不输入用户名
        self.mine_page.input_password("testpass")
        self.mine_page.click_agree()
        self.mine_page.click_login()
        # 验证是否有错误提示（根据实际情况调整断言）
        # 这里可以根据实际需求添加断言逻辑
        result = self.mine_page.get_login_result()
        log.info(f"登录结果: {result}")

    def test_login_with_empty_password(self):
        """测试密码为空的登录场景"""
        # 只输入用户名，不输入密码
        self.mine_page.input_username("testuser")
        self.mine_page.click_agree()
        self.mine_page.click_login()
        # 验证是否有错误提示（根据实际情况调整断言）
        # 这里可以根据实际需求添加断言逻辑