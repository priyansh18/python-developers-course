from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
  

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.maximize_window()

browser.get("https://opensource-demo.orangehrmlive.com")
parentWindow = browser.current_window_handle
print(parentWindow)
browser.find_element(By.XPATH,"//img[@alt='LinkedIn OrangeHRM group']").click()

child_windows = browser.window_handles
print(child_windows)


for child in child_windows:
    print(child)
    if parentWindow!=child:
        print("Switching to new window/tab")
        browser.switch_to.window(child)

browser.quit()
