import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:/Browser drivers/chromedriver_win32/chromedriver.exe")
a=webdriver.Chrome(service=serv_obj)
a.get("https://demo.nopcommerce.com/register")
'''#1.find_element:(3 scenario)
#1.locator matching with single element
element=a.find_element(By.XPATH,"//input[@id='small-searchterms']")
element.send_keys("redmi")
#2.locator matching with multiple elements
elements=a.find_element(By.XPATH,"//div[@class='footer-upper']//a")
print(elements.text)
l=a.find_element(By.PARTIAL_LINK_TEXT,"Log in")
l.click()
time.sleep(10)
a.close()'''
#3.no element in page through exceptional error.
#2.Find_elements:
#1.locator matching with single element
elements=a.find_elements(By.XPATH,"//input[@id='small-searchterms']")
print(len(elements))
#2.locator matching with multiple elements
elements=a.find_elements(By.XPATH,"//div[@class='footer-upper']//a")
print(len(elements))
print(elements[0].text)
print(elements[1].text)
for text in elements:(#use loop to print all text)
    print(text.text)
#3.no element in page does not through exceptional error