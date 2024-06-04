import json
import logging
import os
import pytest
from utils.WebDriverFactory import WebDriverFactory
import pytest_html
import allure
from allure_commons.types import AttachmentType
from datetime import datetime
from pathlib import Path

DEFAULT_CONFIG_PATH = "config.json"
BASE_URL = ""


def pytest_addoption(parser):
    """ Parse pytest --option variables from shell """
    parser.addoption('--config', help='Path to the configuration file to use',
                     default=DEFAULT_CONFIG_PATH)
    parser.addoption('--env', help='Test environment name',
                     default='SIT')


@pytest.fixture
def config_arg(request):
    """:returns config file path from --config option"""
    return request.config.getoption('--config')


@pytest.fixture
def get_test_env(request):
    """:returns test env from --env option"""
    return request.config.getoption('--env')


@pytest.fixture
def config(config_arg):
    logging.basicConfig()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    #Read config file
    logging.info(f'config file path: {config_arg}')

    with open(os.path.join(os.path.dirname(__file__), config_arg)) as config_file:
        config = json.load(config_file)

    return config


#set up webdriver fixture
@pytest.fixture(scope="function", autouse=True)
def driver(config, get_test_env):
    """ Select configuration depends on browser and host"""
    driver = WebDriverFactory().get_driver(config)
    logging.info(f"Test env : {get_test_env}")

    #modify test url based on test env
    #driver.get(f'https://amazon.{get_test_env}.in')

    driver.get("https://amazon.in")

    driver.implicitly_wait(config["implicit_wait"])

    yield driver
    driver.quit()

    # set up a hook to be able to check if a test has failed.


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    driver = item.funcargs['driver']
    if report.when == "call":
        # always add url to report
        extras.append(pytest_html.extras.url(BASE_URL))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.scenario['name'] + " " + datetime.now().strftime("%S%H%d%m%Y") + ".png"
            take_screenshot(driver, file_name)
            if file_name:
                screenshot_dir_path = " .. /screenshots/" + file_name
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick = "window.open(this.src)" align = "right"/></div>' % screenshot_dir_path
                extras.append(pytest_html.extras.html(html))
                allure.attach(driver.get_screenshot_as_png(), name=file_name, attachment_type=AttachmentType.PNG)
        report.extras = extras


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = Path('reports/html_report')
    report_dir.mkdir(parents=True, exist_ok=True)
    pytest_html_path = report_dir / "report.html"
    config.option.htmlpath = pytest_html_path
    config.option.self_contained_html = True


def take_screenshot(driver, file_name):
    report_dir = Path('reports/html_report')
    report_dir.mkdir(parents=True, exist_ok=True)
    driver.save_screenshot(report_dir / file_name)


def pytest_html_report_title(report):
    report.title = "Automation Report"
