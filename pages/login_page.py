from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath: str = '//span[1]'

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def enter_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sing_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def click_on_the_sign_in_button(self):

     def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

        pass

    def title_of_page(self):
        pass

    def wait_for_button_will_be_clicable(self):
        pass
