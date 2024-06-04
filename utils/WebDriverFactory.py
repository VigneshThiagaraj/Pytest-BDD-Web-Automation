import os
import urllib3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class WebDriverFactory:
    def get_driver(self, config):
        """ Disable SSL verification """
        os.environ['WDM_SSL_VERIFY'] = '0'
        """ Ignore InsecureRequestWarning """
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        if config['browser'] == 'firefox':
            firefox_options = webdriver.FirefoxOptions()
            options = self.set_driver_options(config, firefox_options)
            driver = webdriver.Firefox(service= FirefoxService(GeckoDriverManager().install()), options=options)
        elif config['browser'] == 'chrome':
            chrome_options = webdriver.ChromeOptions()
            options = self.set_driver_options(config, chrome_options)
            driver = webdriver.Chrome(service= ChromeService(ChromeDriverManager().install()), options=options)
        else:
            raise Exception(f'Browser "{config["browser"]}" is not supported')
        return driver

    @staticmethod
    def set_driver_options(config, options):
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('start-maximized')
        options.add_argument('window-size=1920*1080')
        options.set_capability("se:recordVideo", "true")
        options.set_capability("se:screenResolution", "1920*1080")
        if config['headless']:
            options.add_argument('headless')

        return options
