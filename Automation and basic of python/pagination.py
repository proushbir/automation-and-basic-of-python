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
website_url="https://www.sharesansar.com/company/niblace"

#open the website url
driver.get(website_url)

#maximize the window
driver.maximize_window()

time.sleep(2)

# search=driver.find_element(*(By.XPATH,"//input[@id='company_search']"))
# search.send_keys("(NIBLACE)")
#
# options_xpath="//li[contains(text(), '(NIBLACE) NIBL Ace Capital Limited')]"
#
# options=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,options_xpath)))
# options.click()

news=driver.find_element(*(By.XPATH,"//a[@id='btn_cnews']"))
news.click()


options=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[normalize-space()='2']")))
options.click()

time.sleep(2)

options2=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[normalize-space()='3']")))
options2.click()

time.sleep(2)

driver.quit()