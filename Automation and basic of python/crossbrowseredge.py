from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

driver=webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

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