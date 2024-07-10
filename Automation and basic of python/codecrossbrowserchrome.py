#import the necessary module
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

#set the chromedriber manager
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

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