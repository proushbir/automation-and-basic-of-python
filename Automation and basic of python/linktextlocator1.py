from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#set the chromedriber manager
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#get the website url:
website_url="https://merolagani.com/"

#open the website url
driver.get(website_url)

#maximize the window
driver.maximize_window()

time.sleep(2)

market=driver.find_element(*(By.XPATH,"//a[normalize-space()='Market']"))
market.click()

time.sleep(2)

indices=driver.find_element(By.LINK_TEXT,"Indices")
indices.click()

time.sleep(3)

print("successfully located the drop down menu")
#close the webdriver
driver.quit()