# pytest:自动化测试框架（三个必须）
import pytest
from script import log
from tools import read_json


class TestLogin:

    @pytest.mark.parametrize("username,password,expect", read_json("login_data.json"))
    def test_01_login(self, enter_mine, username, password, expect):
        """测试登录成功"""
        # 调用方法
        enter_mine.login(username, password)
        # 打印结果
        result = enter_mine.get_toast()
        log.info(f"登录结果：{result}")
        # 断言
        assert expect in result