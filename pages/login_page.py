from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath: str = '//span[1]'
    login_url = 'https://scouts-test.futbolkolektyw.pl/en/login'

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def enter_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_sing_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        test_title = self.get_page_title(self)
        assert self.get_page_title() == self.expected_title

    def wait_for_button_will_be_clicable(self):

        pass