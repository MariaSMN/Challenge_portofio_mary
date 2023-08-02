from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title: str = 'Scouts panel'
    dashboard_url: str = 'http://scouts-test.futbolkolektyw.pl/en/login'
    futbol_kolektyw_logo_xpath = '//*[@title="Logo Scouts Panel"]'

    def title_of_page(self):
        self.wait_for_element_to_be_clicable()
        assert self.get_page_title() == self.expected_title

    def click_add_player_button(self):
        self.click_on_the_element(self.addplayer_button_xpath)

    def type_in_name(self, name):
        self.field_send_keys(self.type_in_name_xpath, name)

    playerscount_label_xpath = "//*[text()='Players']"
    matchescount_label_xpath = "//*[text()='Matches count']"
    reportscount_label_xpath = "//*[text()='Reports count']"
    eventscount_label_xpath = "//*[text()='Events count']"
    devteamcontact_href_xpath = "//a[contains(@href, '://app.slack.com/client/T3X4CAKNU/C3XTEGXB6')]"
    devteamcontact_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[1]/div/div[3]/a/span[1]"
    addplayer_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    lastupdatedplayer_button_xpath = "//div[@class='MuiCardContent-root']/a[2]/button/span[1]"
    lastcreatedplayer_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[1]/button/span[1]"
    signout_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    type_in_name_xpath = "///div[2]/div/div[2]/div/div/input"
    type_in_surname_xpath = "//div[2]/div/div[3]/div/div/input"
    type_in_age_xpath = "//div[2]/div/div[7]/div/div/input"
    type_in_main_position_xpath = "//div[2]/div/div[11]/div/div/input"
    click_submit_button_xpath = "//div[2]/form/div[3]/button[1]/span[2]"

    def wait_for_element_to_be_clicable(self):
        pass
