from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj= Service("C:/Browser drivers/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service =serv_obj )
driver.get("https://money.rediff.com/sectors/bse/bse-it")
driver.maximize_window()
#(1.Self:we assign this element as self node)
'''a = driver.find_element(By.XPATH,"//a[contains(text(),'D-Link (India) Ltd')]/self::a").text#(we assign self keyword we assign a element as self node)
print(a)
driver.close()'''
#2.parent(taking D -link as self node and find the parent node)
'''a=driver.find_element(By.XPATH,"//a[contains(text(),'D-Link (India) Ltd')]/parent::td").text
print(a)
driver.close()'''
#3.Child(explanation in notes)(text syntax for capture a single element)
'''a = driver.find_element(By.XPATH,"//a[contains(text(),'D-Link (India) Ltd')]/ancestor::tr/child::td").text
x = driver.find_elements(By.XPATH,"//a[contains(text(),'D-Link (India) Ltd')]/ancestor::tr/child::td")
print(a)
print(len(x))
driver.close()'''
#4.Ancestor(get the data of childs)
'''a = driver.find_element(By.XPATH,"//a[contains(text(),'D-Link (India) Ltd')]/ancestor::tr").text
print(a)
print(len(a))
driver.close()'''
#5.Following
'''a = driver.find_elements(By.XPATH,"//a[contains(text(),'D-Link (India) Ltd')]/self::a/following::*")
print(len(a))
driver.close()'''
#6.descendant
'''a = driver.find_elements(By.XPATH,"//a[contains(text(),'D-Link (India) Ltd')]/ancestor::tr/descendant::*")
print(len(a))
driver.close()'''
#7.following-sibling
'''a = driver.find_elements(By.XPATH,"//a[contains(text(),'D-Link (India) Ltd')]/self::a/following-sibling::*")
print(len(a))
driver.close()'''
#8.preceding:
'''a = driver.find_elements(By.XPATH,"//a[contains(text(),'D-Link (India) Ltd')]/self::a/preceding::*")
print(len(a))
driver.close()'''
#9.preceding-sibling:
'''a = driver.find_elements(By.XPATH,"//a[contains(text(),'D-Link (India) Ltd')]/self::a//preceding-sibling::a")
print(len(a))
driver.close()'''
#EG1:
a = driver.find_elements(By.XPATH,"//a[contains(text(),'D-Link (India) Ltd')]/ancestor::tr//preceding-sibling::tr")
print(len(a))
driver.close()





