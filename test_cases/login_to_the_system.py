import os
import time
import unittest

import webdriver_manager.core.utils
from selenium import webdriver

import pages.base_page
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service


class TestLoginPage(unittest.TestCase):

    driver = webdriver_manager.core.utils.windows_browser_apps_to_cmd()

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en/login/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user02@getnada.com')
        user_login.enter_password('Test-1234')
        user_login.click_sign_in_button()
        time.sleep(5)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        pages.base_page.tearDown(self)
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
