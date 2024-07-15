from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#set the chromedriber manager
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#get the website url:
website_url="https://meroshare.cdsc.com.np/#/login"

#open the website url
driver.get(website_url)

#maximize the window
driver.maximize_window()

time.sleep(2)

depository=driver.find_element(*(By.XPATH,"/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[1]/div/div/select2/span/span[1]/span/span[1]"))
depository.click()

time.sleep(2)

options_xpath="//li[contains(text(), 'NABIL BANK LIMITED (15100)')]"

options=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,options_xpath)))
options.click()

time.sleep(3)

print("successfully located the drop down menu")
#close the webdriver
driver.quit()