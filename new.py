import os

import time
from selenium import webdriver
import webbrowser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, select
import pywinauto
from pywinauto.application import Application


driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://10.14.48.60")

driver.maximize_window()

button1 = driver.find_element_by_id("details-button")
button1.click()
driver.get ("chrome-error://chromewebdata/#")

link = driver.find_element_by_id("proceed-link")
link.click()

namebox = driver.find_element_by_name("userName")
namebox.send_keys("Nemuadmin")
passbox = driver.find_element_by_name("password")
passbox.send_keys("nemuuser")

button2 = driver.find_element_by_class_name("login-buttons")
button2.click()




button3 = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/ui-modal-renderer/login-banner-modal/ui-modal/div/div/div[3]/div/ui-footer/div/ui-button[1]/button")))

button3.click()

software = driver.find_element_by_xpath("//nav-item[5]//div[1]//nav-menu-link[1]//span[1]//i[2]")
software.click()

softmng = driver.find_element_by_xpath("//span[contains(text(),'Software Management')]")
softmng.click()

time.sleep(5)

soft_update = driver.find_element_by_xpath("//a[contains(text(),'Software Update')]")
soft_update.click()

#browse = driver.find_element_by_xpath("//button[contains(text(),'Browse...')]")
#browse.click()
time.sleep(10)

#driver.execute_script('document.getElementById("local-sw-version").removeAttribute("readonly")')
fileinput = driver.find_element_by_xpath("//ui-file-input[@class='ng-scope ng-isolate-scope']//input").send_keys("C:\AirScale-0.800.1494_ASIB_ABIO.zip")





#dialogwindow = pywinauto.application.Application()
#windowHandle = pywinauto.findwindows.find_window(title=u'Open')
#window = dialogwindow.window(handle=windowHandle)
#toolbar = pywinauto.findwindows.find_element(class)
#toolbar.TypeKeys("C:\download")
