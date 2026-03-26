# pytest:自动化测试框架（三个必须）
import pytest

from base import log
from page.page_home import PageHome
from page.page_mine import PageMine
from tools import DriverTools


class TestLogin:

    version="3.0"

    #失败重新执行
    @pytest.mark.flaky(reruns=2,reruns_delay=1)
    def test_01_login_success(self,enter_mine):
        """测试登录成功"""
        # 调用方法
        enter_mine.login("13800000001", "123456")
        # 打印结果
        result = enter_mine.get_toast()
        log.info(f"登录结果：{result}")
        # 断言
        assert "登录成功" in result

    @pytest.mark.ship(reason="功能未实现")
    def test_02_login_fail_pwd_error(self,enter_mine):
        """测试登录成功"""
        # 调用方法
        enter_mine.login("13800000001", "1234")
        # 打印结果
        result = enter_mine.get_toast()
        log.info(f"登录结果：{result}")
        # 断言
        assert "密码错误" in result
    @pytest.mark.shipif(version="1.0",reason="当前版本跳过")

    def test_03_login_fail_user_not_exist(self,enter_mine):
        """测试登录成功"""
        # 调用方法
        enter_mine.login("13800000005", "123456")
        # 打印结果
        result = enter_mine.get_toast()
        log.info(f"登录结果：{result}")
        # 断言
        assert "账号不存在" in result