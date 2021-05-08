# How To Fix find_element_by_* commands are deprecated warning.

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

browser.maximize_window()
browser.get("https://opensource-demo.orangehrmlive.com")
# browser.find_element(By.NAME, "txtUsername").send_keys("Admin")
# browser.find_element(By.ID, "txtPassword").send_keys("admin123")
# browser.find_element(By.CLASS_NAME, "button").click()
# # browser.find_element_by_name("txtUsername").send_keys("Admin")
# # browser.find_element_by_id("txtPassword").send_keys("admin123")
# # browser.find_element_by_class_name("button").click()
# # Quit is the method of Stopping the application
browser.find_element(By.XPATH, "//input[@id='txtUsername']").send_keys("Admin")
browser.find_element(
    By.CSS_SELECTOR, "//input[type='password']").send_keys("admin123")
browser.find_element(By.XPATH, "//input[@value='LOGIN']").click()
browser.quit()
