from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import glob


list = []

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://10.14.48.60/")
driver.maximize_window()

button1 = driver.find_element_by_id("details-button")
button1.click()
driver.get("chrome-error://chromewebdata/#")

link = driver.find_element_by_id("proceed-link")
link.click()

namebox = driver.find_element_by_name("userName")
namebox.send_keys("Nemuadmin")
passbox = driver.find_element_by_name("password")
passbox.send_keys("nemuuser")

button2 = driver.find_element_by_class_name("login-buttons")
button2.click()

time.sleep(15)

# button3 = driver.find_elements_by_css_selector('body > div.modal.ng-scope.ng-isolate-scope.in > div > div > ui-modal-renderer > login-banner-modal > ui-modal > div > div > div.modal-footer > div > ui-footer > div > ui-button:nth-child(1) > button')
button3 = driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/ui-modal-renderer/login-banner-modal/ui-modal/div/div/div[3]/div/ui-footer/div/ui-button[1]/button')
button3.click()

diagnostic = driver.find_element_by_xpath(
    '//*[@id="main-view"]/div/div[1]/app-header/main-menu/nav-item[6]/div/nav-menu-link/span')
diagnostic.click()

snapshot = driver.find_element_by_xpath(
    '//*[@id="main-view"]/div/div[1]/app-header/main-menu/nav-item[6]/div/ng-transclude/div/div[7]/nav-link/a')
snapshot.click()

collect = driver.find_element_by_xpath(
    '//*[@id="main-view"]/div/div[1]/div[2]/ng-view/wf-panel/wf-panel-section/div/div/div/div[1]/div/div[2]/ui-button/button')
collect.click()

time.sleep(500)

list = os.listdir("C:/Users/tlazaar/Downloads")
for name in list :
    if "Snapshot" in name :
        print(name)
        print("download done")
        break
    else :
        print("download failed")




