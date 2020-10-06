import os

import time
from selenium import webdriver
import os.path

from pathlib import Path

import webbrowser



sw_link = input("Please provide sw download link :")

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get(sw_link)

driver.maximize_window()

username = driver.find_element_by_name("USER")
username.send_keys("tlazaar")
password = driver.find_element_by_name("PASSWORD")
password.send_keys("TTll1999!")

submit = driver.find_element_by_id("submit")
submit.click()

time.sleep(5)

title = driver.find_element_by_id("page-title").text
print(title)

reference = title[-4:]
reference2 = " "
download = driver.find_element_by_xpath("//a[@id='ui-id-8']")
download.click()

time.sleep(15)

sw = driver.find_elements_by_partial_link_text("AirScale-0.800."+reference+"_")


for elem in sw :
    if "ASIB_ABIO" in elem.text :
        elem.click()
        reference2 = elem.text


print(reference2)

f = "C:/Users/tlazaar/Downloads/" + reference2

while not os.path.exists(f):
    time.sleep(1)

if os.path.isfile(f):
    print("file is downloaded")
else :
    print("download failed")

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


time.sleep(15)

button3 = driver.find_element_by_xpath('/html/body/div[1]/div/div/ui-modal-renderer/login-banner-modal/ui-modal/div/div/div[3]/div/ui-footer/div/ui-button[1]/button')
button3.click()

software = driver.find_element_by_xpath("//nav-item[5]//div[1]//nav-menu-link[1]//span[1]//i[2]")
software.click()

softmng = driver.find_element_by_xpath("//span[contains(text(),'Software Management')]")
softmng.click()

time.sleep(5)

soft_update = driver.find_element_by_xpath("//a[contains(text(),'Software Update')]")
soft_update.click()
time.sleep(10)

print (f)
fileinput = driver.find_element_by_xpath("//ui-file-input[@class='ng-scope ng-isolate-scope']//input").send_keys(str(f))
start = driver.find_element_by_xpath("//body[@class='ng-scope']/main-view[@id='main-view']/div[@class='app-root ng-scope']/div[@class='nokia-layout']/div[@class='main-view']/ng-view[@class='view-container ng-scope']/wf-panel[@class='swm-view-panel view-panel ng-scope ng-isolate-scope']/wf-panel-section[@class='view-panel-body panel-body ng-isolate-scope']/div[@class='panel-section']/div[@class='view-panel-body panel-body ng-scope']/software-management[@class='ng-scope ng-isolate-scope']/wf-tabs[@class='software-mgmt-tabs ng-isolate-scope']/div[@class='tab-content']/wf-pane[@class='ng-scope ng-isolate-scope']/div/div[@class='tab-pane ng-class:{active:$ctrl.selected} active']/div[@class='ng-scope']/software-update[@class='ng-isolate-scope']/div[@class='software-update-root']/ui-button[1]")
start.click()


@pytest.fixture(pa)

