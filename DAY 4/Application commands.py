#1.Application commands:
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:/Browser drivers/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#1.title(Used to get a title name):
print(driver.title)
act_title="OrangeHRM"
if act_title==driver.title:
    print("yes")
#2.current_url:
print(driver.current_url)
#3.Page souece:
print(driver.page_source)
driver.close()