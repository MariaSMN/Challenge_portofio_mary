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
    driver_service = None
    driver = webdriver_manager.core.utils.windows_browser_apps_to_cmd()

    @classmethod
    def setUp(cls):
        os.chmod(DRIVER_PATH, 755)
        cls.driver_service = Service(executable_path=DRIVER_PATH)
        cls.driver = webdriver.Chrome(service=cls.driver_service)
        cls.driver.get('https://dareit.futbolkolektyw.pl/en/')
        cls.driver.get('https://dareit.futbolkolektyw.pl/en/')
        cls.driver.fullscreen_window()
        cls.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user02@getnada.com')
        user_login.enter_password('Test-1234')
        user_login.click_sign_in_button()
        time.sleep(5)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        pages.base_page.teardown()
        pages.base_page.BasePage.setup(self)
        time.sleep(15)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()
