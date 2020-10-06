
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


reset_failed = 0
reset_success = 0
nb_of_resets = int (input("Enter number of resets you want to perform:"))
test_line_link =input("Please provide your test line link :")

def snapshotcollect () :
    diagnostic = driver.find_element_by_xpath(
        '//*[@id="main-view"]/div/div[1]/app-header/main-menu/nav-item[6]/div/nav-menu-link/span')
    diagnostic.click()

    snapshot = driver.find_element_by_xpath(
        '//*[@id="main-view"]/div/div[1]/app-header/main-menu/nav-item[6]/div/ng-transclude/div/div[7]/nav-link/a')
    snapshot.click()

    collect = driver.find_element_by_xpath(
        '//*[@id="main-view"]/div/div[1]/div[2]/ng-view/wf-panel/wf-panel-section/div/div/div/div[1]/div/div[2]/ui-button/button')
    collect.click()
    time.sleep(300)


driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get(test_line_link)
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

#button3 = driver.find_elements_by_css_selector('body > div.modal.ng-scope.ng-isolate-scope.in > div > div > ui-modal-renderer > login-banner-modal > ui-modal > div > div > div.modal-footer > div > ui-footer > div > ui-button:nth-child(1) > button')
button3 = driver.find_element_by_xpath('/html/body/div[1]/div/div/ui-modal-renderer/login-banner-modal/ui-modal/div/div/div[3]/div/ui-footer/div/ui-button[1]/button')
button3.click()

#time.sleep(5)
for i in range (nb_of_resets):

    reset= WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="main-view"]/div/div[1]/div[2]/ng-view/wf-panel/wf-panel-section/div/div/site-runtime-views/div/div/div[1]/simplified-site-tab/toolbar/execution-bar/div/reset-site-button/div/ui-button/button')))
    reset.click()



    #reset = driver.find_element_by_css_selector('#main-view > div > div.nokia-layout > div.main-view > ng-view > wf-panel > wf-panel-section > div > div > site-runtime-views > div > div > div.tab-pane.ng-scope.active > simplified-site-tab > toolbar > execution-bar > div > reset-site-button > div > ui-button > button')
    #reset.click()

    time.sleep(5)


    reset2 = driver.find_element_by_css_selector('body > div.modal.reset-site-operations.ng-scope.ng-isolate-scope.in > div > div > common-modal > div > div > div.modal-footer > div > modal-footer > ui-button:nth-child(1) > button')
    reset2.click()


    closewindow = WebDriverWait(driver, 180).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/ui-modal-renderer/bts-status-modal/ui-modal/div/div/div[3]/div/ui-footer/div/ui-button/button')))
    closewindow.click()
    time.sleep(360)
    message = driver.find_element_by_xpath('//*[@id="main-view"]/div/div[1]/div[1]/div/div[2]/cells-delivery/cells-status/div/div[1]').text
    print (message)
    #assert "air" in message
    #closewindow = driver.find_element_by_xpath('/html/body/div[1]/div/div/ui-modal-renderer/bts-status-modal/ui-modal/div/div/div[3]/div/ui-footer/div/ui-button/button')
    if message != "On air" :
        snapshotcollect()
        driver.back()
        reset_failed += 1
        print("reset failed")
    else :
        reset_success +=1
        print("successful reset")



print("number of successful resets :", reset_success)
print("number of failed resets :", reset_failed)

