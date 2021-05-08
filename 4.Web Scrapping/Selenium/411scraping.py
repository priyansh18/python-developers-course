from selenium import webdriver

browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
# Get is the method of starting the application


# myPageTitle = browser.title
# print(myPageTitle)

browser.maximize_window()
browser.get("https://opensource-demo.orangehrmlive.com")


username = browser.find_element_by_name("txtUsername")
enableStatus = username. is_enabled()
displayStatus = username.is_displayed()

print(enableStatus, displayStatus)

username.clear()

attrData = username.get_attribute("type")
fontValue = username.value_of_css_property("font-size")

print(attrData, fontValue)

username.send_keys("Admin")
password = browser.find_element_by_id("txtPassword")
password.send_keys("admin123")
loginButton = browser.find_element_by_class_name("button")
loginButton.click()
# Quit is the method of Stopping the application
browser.quit()
