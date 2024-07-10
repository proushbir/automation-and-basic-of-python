#import the necessary modules
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time

#set the firefox driver
driver=webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

#set the website
website_url='https://www.mindrisers.com.np/'

#get the website
driver.get(website_url)
time.sleep(3)

#maximuize the window size

driver.maximize_window()

time.sleep(3)

#extract the website title
website_title=driver.title
print(f"Website title:{website_title}")
print("congrats!! code executed successfully")

#finally quit the driver instance
driver.quit()