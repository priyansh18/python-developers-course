# Handle DropDown
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

browser.maximize_window()
browser.get("https://www.facebook.com")

browser.find_element(By.XPATH, "//a[text()='Create New Account']").click()
time.sleep(3)


month = browser.find_element(By.ID, "month")
monthDropdown = Select(month)

ddList = monthDropdown.options

defaultItem = monthDropdown.first_selected_option
print("Default", defaultItem.text)


for ele in ddList:
    if ele.text == 'Nov':
        ele.click()
        break
# # March (Month,jan,feb,march,...... )
# monthDropdown.select_by_index(3)
# time.sleep(3)

# # June
# monthDropdown.select_by_value("6")
# time.sleep(3)

# August
# monthDropdown.select_by_visible_text("Aug")
# time.sleep(3)


browser.quit()
