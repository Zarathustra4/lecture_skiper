from tokenize import group
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("D:\Programming\launcher\chromedriver.exe")

schedule_url = "http://asu.pnu.edu.ua/cgi-bin/timetable.cgi?n=700"

browser.get(schedule_url)

group_name = "ІПЗ-11"
group_input = browser.find_element_by_id("group")
group_input.send_keys(group_name)
group_input.send_keys(Keys.ENTER)

