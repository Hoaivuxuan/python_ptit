from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#  khai bao bien browser
browser = webdriver.Chrome(executable_path="chromedriver.exe")
# open web
browser.get("http://facebook.com")
txtUser = browser.find_element("id", "email")
txtUser.send_keys("vuhoai2810@gmail.com")
txtPass = browser.find_element("id", "pass")
txtPass.send_keys("Hoai2002.")
# login facebook
txtPass.send_keys(Keys.ENTER)
sleep(8)
browser.close()