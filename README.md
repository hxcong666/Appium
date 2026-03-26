# AppProject1

一个基于 **Python + Appium + Pytest** 的移动端 UI 自动化测试项目，采用 **POM（Page Object Model）** 组织页面对象，覆盖了 tpshop App 的核心业务流程：

- 登录
- 搜索
- 加购
- 下单

---

## 1. 项目特性

- 使用 `Appium` 驱动 Android 端 UI 自动化
- 使用 `Pytest` 组织测试、Fixture 管理前后置
- 使用页面对象模式（POM）解耦测试逻辑与元素定位
- 内置日志模块（按天滚动）
- 支持 Allure 测试报告生成

---

## 2. 技术栈

- Python 3.x
- Appium Python Client
- Selenium
- Pytest
- Allure-Pytest

---

## 3. 目录结构

```text
AppProject1/
├─ base/                  # 基础层（基类、日志入口）
│  ├─ __init__.py
│  └─ page_base.py
├─ page/                  # 页面对象层（POM）
│  ├─ page_home.py
│  ├─ page_mine.py
│  ├─ page_search.py
│  ├─ page_cart.py
│  └─ page_order.py
├─ script/                # 测试用例层
│  ├─ conftest.py
│  ├─ test_01_*.py
│  ├─ test_02_*.py
│  ├─ test_03_*.py
│  └─ test_04_order.py
├─ config.py              # Appium、设备、应用、等待时间配置
├─ tools.py               # 驱动工具、数据读取、日志工具
├─ pytest.ini             # Pytest 配置
├─ cmd_allure.py          # 生成 Allure HTML 报告脚本
└─ tpshopAPP.apk          # 被测 App 安装包
```

---

## 4. 环境准备

### 4.1 安装依赖

建议先创建虚拟环境，再安装依赖：

```bash
pip install -U pip
pip install appium-python-client selenium pytest allure-pytest pytest-rerunfailures
```

### 4.2 启动 Appium Server

默认配置地址：`http://127.0.0.1:4723/wd/hub`

请确保 Appium 服务已启动，且设备已连接可用。

### 4.3 准备 Android 设备/模拟器

当前默认配置（见 `config.py`）：

- `platformName`: Android
- `platformVersion`: 12
- `deviceName`: mumu
- `appPackage`: com.tpshop.malls
- `appActivity`: .SplashActivity

如与本机环境不一致，请先修改 `config.py`。

---

## 5. 执行测试

在项目根目录运行：

```bash
pytest
```

> 注意：当前 `pytest.ini` 中 `python_files = test_04*.py`，默认只会收集 `test_04` 开头的脚本（即下单相关用例）。
>
> 如果要执行全部用例，可修改 `pytest.ini`，例如改为：
>
> ```ini
> python_files = test_*.py
> ```

### 运行冒烟用例

```bash
pytest -m smoke
```

---

## 6. 生成 Allure 报告

项目默认将原始结果输出到 `report/`（见 `pytest.ini` 的 `--alluredir report`）。

执行以下命令生成 HTML 报告：

```bash
python cmd_allure.py
```

生成目录为：`new_report/`。

---

## 7. 框架说明（简要）

- `base/page_base.py`：封装基础操作（显式等待、点击、输入、取文本、滑动、Toast 获取）
- `page/*.py`：页面对象，封装元素定位和业务动作
- `script/conftest.py`：统一管理驱动创建、页面跳转、登录/搜索/加购等复用前置流程
- `tools.py`：驱动单例工具、JSON 数据读取、日志工具

---

## 8. 常见问题

1. **连接失败**：检查 Appium 地址、端口、设备连接状态。
2. **元素定位超时**：确认当前页面状态是否正确，必要时增加等待或优化定位方式。
3. **Toast 获取为空**：Toast 展示时间短，建议在触发后立即等待并读取。
4. **Allure 命令不可用**：需先安装并配置 Allure Commandline。

---

## 9. 后续建议

- 增加 `requirements.txt` 统一依赖管理
- 补充 `data/` 测试数据文件并完善数据驱动测试
- 接入 CI（如 GitHub Actions/Jenkins）实现自动执行与报告归档
- 增加失败截图与日志附件到 Allure 报告

---

## 10. 说明

本项目主要用于 App 自动化测试学习与实践，可作为中小型移动端 UI 自动化项目模板使用。
