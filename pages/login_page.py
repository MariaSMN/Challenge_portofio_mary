from selenium.webdriver.chrome.webdriver import WebDriver

from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = '//span[1]'
    login_url = 'https://dareit.futbolkolektyw.pl/en/'
    add_player_button = "//div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.addplayer_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
        self.expected_title = "Scouts Panel"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def enter_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def title_of_page(self):
        self.get_page_title()
        assert self.expected_title == self.get_page_title()

    def wait_for_button_will_be_clicable(self):
        pass

    def click_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def click_add_player_button(self):
        self.click_on_the_element(self.addplayer_button_xpath)

    def click_on_the_sign_in_button(self):
        pass
