from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd


browser = webdriver.Chrome(ChromeDriverManager().install())

browser.maximize_window()

browser.get("https://www.amazon.in")
browser.find_element(By.XPATH,"//input[contains(@id,'search')]").send_keys('Samsung Phones')
browser.find_element(By.XPATH,"//input[contains(@id,'nav-search-submit-button')]").click()
browser.find_element(By.XPATH,"//span[text()='Samsung']").click()
phoneNames = browser.find_elements(By.XPATH,"//span[contains(@class,'a-color-base a-text-normal')]")
phonePrices = browser.find_elements(By.XPATH,"//span[contains(@class,'price-whole')]")

myPhone = []
myPrice = []
for phoneName in phoneNames:
    myPhone.append(phoneName.text)

for phonePrice in phonePrices:
    myPrice.append(phonePrice.text)

finalList = zip(myPhone,myPrice)

print(finalList)

df = pd.DataFrame(finalList, columns =['Phone_Name', 'Phone_Price'])

print(df)

df.to_csv('phones.csv')
browser.quit()
