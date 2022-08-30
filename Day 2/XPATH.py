#1.Realative X-Path:
#//a href[@class="btn-orange trial-btn pulse"]
#2.Absolute X-Path:
#/html/body/nav/div/div[1]/a/img
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:/Browser drivers/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("http://automationpractice.com/index.php")
driver.maximize_window()
#ABSOLUTE XPATH:
'''driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys("Mens Tshirts")
driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button").click()
driver.close()'''
#RELATIVE XPATH:
'''driver.find_element(By.XPATH,"//*[@id='search_query_top']").send_keys("TSHIRT")
driver.find_element(By.XPATH,"//*[@id='searchbox']/button").click()
driver.close()'''
#OPTION OF XPATH
#1.X-PATH WITH OR:(Atleat one path is crct it is working)
'''driver.find_element(By.XPATH,"//input[@id='search_query_top' or @name='search_query']" ).send_keys("tshirts")
driver.find_element(By.XPATH,".//button[@name='submit_search' or @type='submit']").click()'''
#2.X-PATH WITH AND:(Both should be crct)
'''driver.find_element(By.XPATH,"//input[@id='search_query_top' and @name='search_query']" ).send_keys("tshirts")
driver.find_element(By.XPATH,".//button[@name='submit_search' and @type='submit']").click()'''
#3.X-PATH WITH CONTAINS(Find the common thing in value):
driver.find_element(By.XPATH,"//input[contains(@id,'search')]").send_keys("Printed Chiffon Dress");
driver.find_element(By.XPATH,"//button[contains(@name,'submit_sea')]").click()
driver.close()
#4 X-PATH WITH Starts-with(Starting letters of value sholud be same in that place we use)
'''driver.find_element(By.XPATH,"//a[text()='women']").click()'''