from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObject = Service("C:\Driver\chromedriver.exe")

driver = webdriver.Chrome(service=serviceObject)


driver.get("https://wordpress.com/log-in/")


