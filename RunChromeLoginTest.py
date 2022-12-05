import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.rediff.com/"
username = 'yiroco'
password = 'Password@123'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CLASS_NAME, "signin").click()
time.sleep(2)
driver.find_element(By.ID, "login1").send_keys(username)
time.sleep(2)
driver.find_element(By.ID, "password").send_keys(password)
time.sleep(2)
driver.find_element(By.NAME, "proceed").click()
x = driver.find_element(By.LINK_TEXT, "yi roco")
print(x)
if x == "yi roco":
    print("login failed")
else:
    print("login success")
driver.find_element(By.LINK_TEXT, "Logout").click()

