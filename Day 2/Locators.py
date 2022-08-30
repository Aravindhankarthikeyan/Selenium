#1.BUILT IN LOCATORS()
#1.ID & NAME:(Value of class :"Search items")
'''from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:/Browser drivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/login?returnUrl=%2F")
driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
#2.LINK TEXT/PARTIAL LINK TEXT:(Value of class :"REGISTER")'''
'''from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:/Browser drivers/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/login?returnUrl=%2F")
driver.maximize_window()
#driver.find_element(By.LINK_TEXT,"Register").click()#link text
driver.find_element(By.PARTIAL_LINK_TEXT,"gister").click()#partial link text
driver.close()'''
#3.CLASS NAME & TAG NAME:(Value of class :"homeslider-container")
#class name(sliders):
'''from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:/Browser drivers/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("http://automationpractice.com/index.php")
sliders =driver.find_elements(By.CLASS_NAME,"homeslider-container")
print(len(sliders))'''
#Tag name(Links):
'''from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:/Browser drivers/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("http://automationpractice.com/index.php")
links = driver.find_elements(By.TAG_NAME,"a")
print(len(links))
driver.close()'''



