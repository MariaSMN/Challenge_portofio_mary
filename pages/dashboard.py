import time
from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = 'Scouts panel'
    dashboard_url = "http://scouts-test.futbolkolektyw.pl/en/login"
    futbol_kolektyw_logo_xpath = '//*[@title="Logo Scouts Panel"]'

    def title_of_page(self):
        self.wait_for_element_to_be_clicable()
        assert self.get_page_title() == self.expected_title

    def click_add_player_button(self):
        self.click_on_the_element(self.addplayer_button_xpath)

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

    def wait_for_element_to_be_clicable(self):
        pass
