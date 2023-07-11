import os
import time
import unittest
from selenium import webdriver

import pages.base_page
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
class TestDashboardPage(unittest.TestCase):
    driver_service = None
    driver = None

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_add_player(self, user_login=None):
        pages.base_page.BasePage.setUp(self)
        user_login.click_on_the_add_player_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        pages.BasePage.tearDown(self)
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()



