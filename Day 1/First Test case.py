#Selenium 4:
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("C:/Browser drivers/chromedriver_win32/chromedriver.exe")
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.ID,"txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.ID,"btnLogin").click()
act_title = driver.title
exp_title ="OrangeHRM"
if act_title == exp_title:
    print("login pass")
else:
    print("login failed")


print(driver.title)
driver.close()




