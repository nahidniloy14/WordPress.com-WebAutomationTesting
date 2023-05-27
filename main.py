import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serviceObject = Service("C:\Driver\chromedriver.exe")

driver = webdriver.Chrome(service=serviceObject)

driver.get("https://wordpress.com/log-in/")


#SIGN UP
driver.get("https://wordpress.com/")
driver.find_element(By.XPATH,"//nav/ul[2]/li[2]/a").click()

time.sleep(10)
driver.find_element(By.ID,"email").send_keys("pivil17463@duscore.com")
driver.find_element(By.ID,"username").send_keys("pivil174")
driver.find_element(By.ID,"password").send_keys("p7k3f58C%$.rs4p")
driver.maximize_window()
driver.find_element(By.XPATH,"//div/form/div[2]/button").click()

#LOG IN
driver.find_element(By.CLASS_NAME, "form-text-input").send_keys("nahidniloy894@gmail.com")
time.sleep(8)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

driver.find_element(By.CLASS_NAME,"social-buttons__service-name").click()
print(driver.current_window_handle)

# email input
driver.find_element(By.XPATH,"//input[@id='identifierId']").send_keys("nahidniloy894@gmail.com")
# Submit
driver.find_element(By.XPATH,"//div[@id='view_container']/div/div/div[2]/div/div[2]/div/div[1]/div/div").click()
# Scroll down
driver.execute_script("window.scrollBy(0,7000)","")
#Click Explore Plugin
driver.find_element(By.XPATH,"//div[@class='quick-links__boxes']/a[8]/div/span").click()
