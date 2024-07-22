#import the necessary module
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_google_search():
    # set the chromedriver manager
    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)

    #set the website
    website_url=driver.get("https://www.google.com/")
    search_box=driver.find_element(*(By.XPATH, "//textarea[@id='APjFqb']"))
    search_box.send_keys("mindrisers.cpm.np")
    driver.maximize_window()
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    #click on the available link
    first_link=driver.find_element(*(By.XPATH, "//h3[contains(text(),'Best IT Training Institute in kathmandu, Nepal | M')]"))
    first_link.click()
    time.sleep(2)
    print("Congratz first pytest is successful")
