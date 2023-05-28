import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

serviceObject = Service("C:\Driver\chromedriver.exe")

driver = webdriver.Chrome(service=serviceObject)

driver.get("https://wordpress.com/log-in/")

#1Log in to your WordPress site.
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



#2. Check whether the “WP Dark Mode” Plugin is Active or not.
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


#3.If Active, navigate to the WP Dark Mode & continue. Otherwise, Install the Plugin and Activate it.
#Install
driver.find_element(By.XPATH,"(//ul[@class='plugin-action-buttons'])[1]/li[1]").click()

#Activate
driver.find_element(By.XPATH,"(//ul[@class='plugin-action-buttons'])[1]/li[1]").click()

driver.execute_script("window.scrollBy(0,700)","")

driver.find_element(By.XPATH,"(//input[@id='save_settings'])[1]").click()


#Click Wp Dark Mode
driver.find_element(By.XPATH,"//div[normalize-space()='Settings']").click()

#4.Enable Backend Darkmode from Settings -> General Settings.
#Click General Settings
driver.find_element(By.XPATH,"(//span[contains(text(),'General Settings')])[1]").click()
#Enable Backend Darkmode
driver.find_element(By.XPATH,"(//label[@for='wppool-wp_dark_mode_general[enable_backend]'])[2]").click()


#5.valdiate the dark made working on admin dashboard
toggle_button=driver.find_element(By.XPATH,"wppool-wp_dark_mode_general[enable_frontend]")
dark_mode_active=toggle_button.is_selected()
if dark_mode_active:
    print("Dark mode is active.")
else:
    print("Dark mode is not active.")

#6.Navigate to the WP Dark Mode.
driver.find_element(By.XPATH,"//div[normalize-space()='WP Dark Mode']").click()


#7. From Settings -> Switch Settings - Change the “Floating Switch Style” from the default selections (Select any one from the available options, except the default selected one).
#select switch setting
driver.find_element(By.XPATH,"//a[@id='wp_dark_mode_switch-tab']//span[contains(text(),'Switch Settings')]").click()
#change floating style
driver.find_element(By.XPATH,"//input[@id='wppool-wp_dark_mode_switch[switch_style][3]'])[1]").click()

#8.Select Custom Switch size & Scale it to 220
#select custom size
driver.find_element(By.XPATH,"(//input[@id='wppool-wp_dark_mode_switch[switch_style][3]'])[1]").click()
scale_slider=driver.find_element(By.XPATH,"(//input[@id='wp_dark_mode_switch[switcher_scale]'])[1]").get_property('value')
scale_value=int(scale_slider.get_attribute("value"))
if scale_value != 200:
    driver.execute_script("arguments[0].setAttribute('value', '200')", scale_slider)

#9.From Settings -> Switch Settings - Change the Floating Switch Position (Left Bottom).
dropdown=Select(driver.find_element(By.ID,"wp_dark_mode_switch[switcher_position]"))
dropdown.select_by_visible_text("Left Bottom")
