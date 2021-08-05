from warnings import catch_warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("incognito")
chrome_options.add_argument("start-maximized")
driver = webdriver.Chrome(chrome_options=chrome_options)


driver.get("https://learnweb.csc.cxs.cloud/learner/index.html#/")

# Define Variable
try:
    element = WebDriverWait(driver, 4).until(
        EC.presence_of_all_elements_located((By.ID, "txt-email"))
    )
finally:
    email_input = driver.find_element_by_id("txt-email")
    password_input = driver.find_element_by_id("txt-password")
    email_input.send_keys("refactory07@yopmail.com")
    password_input.send_keys("ABCDE1234567890")
    password_input.send_keys(Keys.ENTER)
try:
    element = WebDriverWait(driver, 7).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".btn-primary"))
    )
finally:
    continue_button = driver.find_element_by_css_selector(".btn-primary")
    continue_button.click()

try:
    discover = WebDriverWait(driver, 12).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".eqwrze13"))        
    )
except:
    print("error, happen cause there are no element")
finally:
    dailyFeed = driver.find_element_by_css_selector(".eqwrze13")    
    print(dailyFeed.value_of_css_property("font-size"))




    
    

    

