from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import smtplib
from email.message import EmailMessage

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

# Zip two lists and convert data into CSV file

finalList = zip(myPhone,myPrice)

df = pd.DataFrame(finalList, columns =['Phone_Name', 'Phone_Price'])

df.to_csv('phones.csv')

# Sending Emails 

msg = EmailMessage()
msg['Subject'] = 'Samsung Scrapped Data'
msg['From'] = 'Automation Team'
msg['To'] = 'spriy89@gmail.com'


with open('EmailTemplate.txt') as myfile:
    data = myfile.read()
    msg.set_content(data)


with open("phones.csv","rb") as f:
    file_data = f.read()
    print("File data in binary file",file_data)
    file_name = f.name
    print('File name is ',file_name)
    msg.add_attachment(file_data,maintype="application",subtype="csv",filename = file_name)


with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
    server.login(Email,password)
    server.send_message(msg)

print('Email Sent')


browser.quit()
