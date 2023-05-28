import time

from selenium import webdriver
from selenium.webdriver import Keys
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
driver.execute_script("window.scrollBy(0,500)","")
#ClickPlugin
driver.find_element(By.XPATH,"//div[@class='quick-links__boxes']/a[8]/div/span").click()
#addnew
driver.find_element(By.XPATH,"//a[@class='page-title-action']").click()
#Click the Search Icon
driver.find_element(By.XPATH,"//div/main/div[1]/div/div/div/button[1]")
#Search WP dark mode
driver.find_element(By.CLASS_NAME,"search-component__input-fade").send_keys("WP dark mode")
#Press Enter
driver.find_element(By.CLASS_NAME,"search-component__input-fade").send_keys(Keys.ENTER)

#Select WP Dark Mode
driver.find_element(By.XPATH,"//div[@class='card plugins-browser-list__elements']/li[1]").click()

#Install
driver.find_element(By.XPATH,"(//ul[@class='plugin-action-buttons'])[1]/li[1]").click()

#Activate
driver.find_element(By.XPATH,"(//ul[@class='plugin-action-buttons'])[1]/li[1]").click()

driver.execute_script("window.scrollBy(0,700)","")

driver.find_element(By.XPATH,"(//input[@id='save_settings'])[1]").click()

#Click Wp Dark Mode
driver.find_element(By.XPATH,"//div[normalize-space()='Settings']").click()
#Click General Settings
driver.find_element(By.XPATH,"(//span[contains(text(),'General Settings')])[1]").click()
#Enable Backend Darkmode
driver.find_element(By.XPATH,"(//label[@for='wppool-wp_dark_mode_general[enable_backend]'])[2]").click()
#valdiate the dark made working on admin dash
toggle_button=driver.find_element(By.XPATH,"wppool-wp_dark_mode_general[enable_frontend]")
dark_mode_active=toggle_button.is_selected()
if dark_mode_active:
    print("Dark mode is active.")
else:
    print("Dark mode is not active.")

