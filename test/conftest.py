import os
import time
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")  # call only once in class level
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")  # get value from command line
    if browser_name == "chrome":
        # service_obj = Service()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    elif browser_name == "firefox":
        pass

    elif browser_name == "IE":
        pass
    driver.implicitly_wait(5)
    driver.get("https://staging.rapiddiecut.com/")
    time.sleep(1)
    driver.maximize_window()

    request.cls.driver = driver  # give our local driver to the class driver by cls.driver

    yield
    time.sleep(4)
    driver.close()


# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#         Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#         :param item:
#         """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             path = "/home/gaurav.gaikwad/AKseleniumFrameworkProject/test/"
#             _capture_screenshot(file_name)
#             file_name = file_name.replace("test/", "")
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % (path + file_name)
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            file_name = file_name.replace("test/", "")
            path = "/home/gaurav.gaikwad/RDC12Selenium/screenshots/" + file_name
            _capture_screenshot(path)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % path
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
