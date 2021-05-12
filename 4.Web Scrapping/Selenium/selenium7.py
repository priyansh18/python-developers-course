from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import datetime

def currentTime():
    return datetime.datetime.now().strftime("%H_%M_%S_%d_%m_%Y")

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://www.google.com')

browser.get_screenshot_as_file('image' + currentTime()+".png")

browser.get('https://www.facebook.com') 

browser.get_screenshot_as_file('image' + currentTime()+".png")

browser.quit()