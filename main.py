import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.maximize_window()
load_dotenv()


# Access the login information
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

#Log in to your WordPress site
driver.get("https://dev-daredreamdo.pantheonsite.io/wp-login.php")

driver.find_element(By.ID,"user_login").send_keys(username)
driver.find_element(By.ID,"user_pass").send_keys(password)
driver.find_element(By.ID,"wp-submit").click()
time.sleep(5)
#Check whether the “WP Dark Mode” Plugin is Active or not.
driver.find_element(By.XPATH,"(//div[@class='wp-menu-name'])[8]").click()
driver.find_element(By.XPATH,"//ul[@class='subsubsub']/li[2]").click()
driver.execute_script("window.scrollBy(0,700)","")
time.sleep(5)
element=driver.find_element(By.XPATH,"//a[@id='deactivate-wp-dark-mode']").text
#text=print(element)
if element == "Deactivate":
    print("Plugin Installed")
else:
    print("Plugin Not Installed")
#assert element == "Deactivate"

#If active: navigate to the WP Dark Mode & continue
driver.find_element(By.XPATH,"//div[normalize-space()='WP Dark Mode']").click()

#Enable Backend Darkmode from Settings -> General Settings.
driver.find_element(By.XPATH,"(//div[@class='wp-dark-mode-ignore'])[2]").click()
driver.find_element(By.XPATH,"(//input[@id='save_settings'])[1]").click()
driver.find_element(By.XPATH,"(//p[@class='dark wp-dark-mode-ignore'])[1]").click()

#Navigate to the WP Dark Mode.
driver.find_element(By.XPATH,"//div[normalize-space()='WP Dark Mode']").click()
"""
#From Switch Settings - Change the “Floating Switch Style” 
driver.find_element(By.XPATH,"//a[@id='wp_dark_mode_switch-tab']//span[contains(text(),'Switch Settings')]").click()
#change floating style
driver.find_element(By.XPATH,"//input[@id='wppool-wp_dark_mode_switch[switch_style][3]'])[1]").click()

#Select Custom Switch size & Scale it to 220.
driver.find_element(By.XPATH,"(//input[@id='wppool-wp_dark_mode_switch[switch_style][3]'])[1]").click()
scale_slider=driver.find_element(By.XPATH,"(//input[@id='wp_dark_mode_switch[switcher_scale]'])[1]").get_property('value')
scale_value=int(scale_slider.get_attribute("value"))
if scale_value != 200:
    driver.execute_script("arguments[0].setAttribute('value', '200')", scale_slider)

#Change the Floating Switch Position (Left Bottom)
dropdown=Select(driver.find_element(By.ID,"wp_dark_mode_switch[switcher_position]"))
dropdown.select_by_visible_text("Left Bottom")
driver.find_element(By.ID,"save_settings").click()
"""
#Disable Keyboard Shortcut from the Accessibility Settings.
driver.find_element(By.XPATH,"(//span[contains(text(),'Accessibility Settings')])[1]").click()
driver.execute_script("window.scrollBy(0,700)","")
time.sleep(7)
driver.find_element(By.XPATH,"(//div[@class='wp-dark-mode-ignore'])[23]").click()
time.sleep(5)
driver.find_element(By.XPATH,"(//input[@id='save_settings'])[8]").click()
time.sleep(5)

#Validate whether the Darkmode is working or not from the Frontend
driver.find_element(By.XPATH,"(//span[contains(text(),'General Settings')])[1]").click()
front_end_active=driver.find_element(By.XPATH,"(//p[normalize-space()='Turn ON to enable the darkmode in the frontend.'])[1]").text
print(front_end_active)
if front_end_active=="Turn ON to enable the darkmode in the frontend.":
    print("Darkmode is not working on the frontend")
else:
    print("Darkmode is working on the frontend")


#Enable “Darkmode Toggle Animation” & change the “Animation Effect”
driver.find_element(By.XPATH,"(//a[@id='wp_dark_mode_animation-tab'])[1]").click()
time.sleep(5)
driver.find_element(By.XPATH,"(//label[@for='wppool-wp_dark_mode_animation[toggle_animation]'])[2]").click()
time.sleep(5)

dropdown=Select(driver.find_element(By.XPATH,"(//select[@id='wp_dark_mode_animation[animation]'])[1]"))
#Change Animation
time.sleep(5)
dropdown.select_by_index("3")
time.sleep(5)
driver.find_element(By.XPATH,"(//input[@id='save_settings'])[13]").click()


# Clean up the driver instance
driver.quit()

#