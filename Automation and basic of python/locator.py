#path locator create and post method
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#set the chromedriber manager
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#get the website url:
website_url="https://demoqa.com/text-box"

#open the website url
driver.get(website_url)

#maximize the window
driver.maximize_window()

time.sleep(2)

#find the form webelement by their xpath
full_name=driver.find_element(By.XPATH,"//input[@id='userName']")
email_field=driver.find_element(By.XPATH,"//input[@id='userEmail']")
current_address_field=driver.find_element(By.XPATH,"//textarea[@id='currentAddress']")
permanent_address_field=driver.find_element(By.XPATH,"//textarea[@id='permanentAddress']")
submit_button=driver.find_element(By.ID,"submit")

#fill the form
full_name.send_keys('ramesh')
email_field.send_keys('ramesh@gmail.com')
current_address_field.send_keys('chyasal')
permanent_address_field.send_keys('nuwakot')
submit_button.click()
time.sleep(4)

#extract the website title
website_title=driver.title
print(f"Website title:{website_title}")

#close the webdriver instance
driver.quit()