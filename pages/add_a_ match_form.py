from pages.base_page import BasePage


class add_a_match_form (BasePage):
    my team_label_xpath = "//*[text()='My team']"
    enemy team_label_xpath = "//*[text()='Enemy team']"
    my team score_label_xpath = "//*[text()='My team score']"
    enemy team score_label_xpath = "//*[text()='Enemy team score']"
    date_label_xpath = "//*[text()='Date']"
    match at home_marker_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[1]/span[2]"
    match out home_marker_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[2]/span[2]"
    submit_button_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[1]/span[2]"
    clear_button_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[2]/span[2]"
    sign out_button_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[3]/div[2]/div[2]/span"


pass