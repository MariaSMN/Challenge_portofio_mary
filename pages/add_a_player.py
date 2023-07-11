import os
import time
import unittest
from selenium import webdriver

from pages.add_a_player import AddAPlayer
import pages.base_page
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
class TestDashboardPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome()
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_a_player(self):
        pages.base_page.BasePage.setUp(self)
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user02@getnada.com')
        user_login.enter_password('Test-1234')
        user_login.click_sign_in_button()
        time.sleep(5)
        dashboard_page = Dashboard(self.driver)
        user_login.click_add_a_player_button()
        time.sleep(5)
        add_a_player = AddAPlayer(self.driver)
        add_a_player.title_of_page()

    @classmethod
    def tearDown(self):
        self.driver.quit()


