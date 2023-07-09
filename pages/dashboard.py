from pages.base_page import BasePage


class Dashboard(BasePage):
    players count_label_xpath = "//*[text()='Players']"
    matches count_label_xpath = "//*[text()='Matches count']"
    reports count_label_xpath = "//*[text()='Reports count']"
    events count_label_xpath = "//*[text()='Events count']"
    dev team contact_href_xpath = "//a[contains(@href, '://app.slack.com/client/T3X4CAKNU/C3XTEGXB6')]"
    dev team contact_button_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[1]/div/div[3]/a/span[1]"
    add player_button_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    last updated player_button_xpath = "//div[@class='MuiCardContent-root']/a[2]/button/span[1]"
    last created player_button_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[1]/button/span[1]"
    sign out_button_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"








    pass