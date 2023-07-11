from pages.base_page import BasePage


class add_a_match_form(BasePage):
    myteam_label_xpath = "//*[text()='My team']"
    enemyteam_label_xpath = "//*[text()='Enemy team']"
    myteamscore_label_xpath = "//*[text()='My team score']"
    enemyteamscore_label_xpath = "//*[text()='Enemy team score']"
    date_label_xpath = "//*[text()='Date']"
    matchathome_marker_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[1]/span[2]"
    matchouthome_marker_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[2]/span[2]"
    submit_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[1]/span[2]"
    clear_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[2]/span[2]"
    signout_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[3]/div[2]/div[2]/span"
