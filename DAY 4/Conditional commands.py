#2.Conditional commands:
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:/Browser drivers/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()
#1.is_Displayed,is_enabled:
searchbox=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print(searchbox.is_displayed())
print(searchbox.is_enabled())
#2.Is_selected:
radiobutton_male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
radiobutton_male.click()
radiobutton_female=driver.find_element(By.XPATH,"//input[@id='gender-female']")
print(radiobutton_male.is_selected())
print(radiobutton_female.is_selected())
driver.close()