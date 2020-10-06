
from selenium import webdriver
import time



driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://10.14.48.60/")

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

#button3 = driver.find_elements_by_css_selector('body > div.modal.ng-scope.ng-isolate-scope.in > div > div > ui-modal-renderer > login-banner-modal > ui-modal > div > div > div.modal-footer > div > ui-footer > div > ui-button:nth-child(1) > button')
button3 = driver.find_element_by_xpath('/html/body/div[1]/div/div/ui-modal-renderer/login-banner-modal/ui-modal/div/div/div[3]/div/ui-footer/div/ui-button[1]/button')
button3.click()

time.sleep(5)
for i in range (3):
    reset = driver.find_element_by_css_selector('#main-view > div > div.nokia-layout > div.main-view > ng-view > wf-panel > wf-panel-section > div > div > site-runtime-views > div > div > div.tab-pane.ng-scope.active > simplified-site-tab > toolbar > execution-bar > div > reset-site-button > div > ui-button > button')
    reset.click()

    time.sleep(5)


    reset2 = driver.find_element_by_css_selector('body > div.modal.reset-site-operations.ng-scope.ng-isolate-scope.in > div > div > common-modal > div > div > div.modal-footer > div > modal-footer > ui-button:nth-child(1) > button')
    reset2.click()
    time.sleep(180)

#alert = driver.switch_to_alert()
#alert.accept()

#driver.get ("https://10.14.48.60/#/login")

#print(driver.title)