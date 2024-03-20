# Steps are given below for this testcases
# open the browser any(chrome/gecko/edge/safari)
# open url
# provide username and password and click to login button
# capture the title of the webpage to validate
# close the browser
# https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
#
from pyautogui import click
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Optionally, add any desired options
# For example, to run Chrome in headless mode:
# chrome_options.add_argument("--headless")
servicePath=Service("C:\\Users\\Acer\\OneDrive\\Desktop\\code\\driver\\chrome\\chromedriver.exe")
# Pass chrome_options object to webdriver.Chrome
driver = webdriver.Chrome(service=servicePath)
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.implicitly_wait(10.0)
user=driver.find_element(By.NAME,"username")
user.send_keys("Admin")
print("Hi")
password=driver.find_element(By.NAME,"password")
password.send_keys("admin123")
driver.find_element(By.XPATH,"//*/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
print("Hi")
login_val=driver.find_element(By.XPATH,"//*/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
print(login_val)
login_exp_val="Dashboard"
if login_val==login_exp_val:
    print("Validated")
else:
    print("Not validated or mismatching")
end = input("Provide any key to quit: Ex: type OK and press Enter ::: ")
driver.quit()
