#2.Customized Locators:
#1.CSS SELECTORS:
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:/Browser drivers/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.facebook.com/")
driver.maximize_window()
#1.TAG & ID:(input#value of ID)
#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
#2.TAG & CLASS:(INPUT.VALUE OF CLASS
#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc@gmail.com")#remove those 55r1 beacuse gap after inputtxt cause errro
#3.TAG & ATTRIBUTE:INPUT[ATTRIBUTE = VALUE]
#driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("abc@gmail.com")
#3.TAG & ATTRIBUTE& CLASS:(these two having same class, name ,id  but diff attribute)
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_email]").send_keys("abc@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("12345")
driver.find_element()
driver.close()

