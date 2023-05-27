from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serviceObject = Service("C:\Driver\chromedriver107.exe")

driver = webdriver.Chrome(service=serviceObject)

driver.get("https://wordpress.com/log-in/")
driver.find_element(By.CLASS_NAME, "form-text-input").send_keys("nahidniloy894@gmail.com")
driver.find_element(By.CLASS_NAME, "button form-button is-primary").click()
