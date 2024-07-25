#import the necessary module
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture()
def driver():
    # set the chromedriver manager
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    # yield the driver
    yield driver
    # close the driver
    driver.quit()

@pytest.mark.parametrize("username,password",[
    ("new","pass"),
    ("malikacounter5", "password"),
    ("admin","passwrod"),
])

def test_login(driver,username,password):
    driver.get("https://tax.digitalpalika.org/login")
    username_field=driver.find_element(*(By.XPATH,"//input[@id='username']"))
    password_field=driver.find_element(*(By.XPATH,"//input[@id='password']"))
    login=driver.find_element(*(By.XPATH,"//button[normalize-space()='Login']"))

    username_field.send_keys(username)
    password_field.send_keys(password)
    login.click()

    try:
        alert=driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        assert "Username or Password is incorrect" in alert_text
        print(f"Username and password is incorrect for {username}")

    except:
        # if there is alert message for successful login
        time.sleep(2)
        # alert = driver.switch_to.alert
        # alert_text1 = alert.text
        # alert.accept()
        # assert "Successfully login!" in alert_text1
        # print(f"Successful login for {username}")
        page_source=driver.page_source
        if "Counter Dashbord" in page_source:
            print(f"Successful login for {username}")
        else:
            print(f"Unexpected error or login failed for {username}")