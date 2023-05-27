import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serviceObject = Service("C:\Driver\chromedriver.exe")

driver = webdriver.Chrome(service=serviceObject)

driver.get("https://wordpress.com/log-in/")
# Sign up
# driver.find_element(By.CLASS_NAME, "form-text-input").send_keys("nahidniloy894@gmail.com")
# time.sleep(8)
# driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

#sign in with Google
driver.find_element(By.CLASS_NAME,"social-buttons__service-name").click()
time.sleep(3)
driver.find_element(By.ID,"identifierId").send_keys("nahidniloy894@gmail.com")
driver.find_element(By.XPATH,"//div[@id='view_container']/div/div/div[2]/div/div[2]/div/div[1]/div/div").click()