from selenium import webdriver
from webdriver_manager.chrome import ChromeDriver, ChromeDriverManager
# from getpass import getpass

browser = webdriver.Chrome(ChromeDriverManager().install())


browser.maximize_window()

browser.get("https://www.codechef.com")

browser.find_element_by_id("edit-name").send_keys("test123_4")
browser.find_element_by_id("edit-pass").send_keys("Test.1234")
browser.find_element_by_id("edit-submit").click()

browser.get("https://www.codechef.com/submit/TEST")

browser.find_element_by_id('edit_area_toggle_checkbox_edit-program').click()

with open('solution.cpp','r') as f:
    code = f.read()

browser.find_element_by_xpath("//span[@class='ace_identifier']").send_keys(code)

browser.find_element_by_id('edit-submit').click()

browser.quit()