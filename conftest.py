import pytest
import paramiko
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import paramiko


@pytest.fixture(scope="class")

def setup_ssh(request):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.load_system_host_keys()

    try:

        client.connect("10.14.48.60", username="toor4nsn", password="oZPS0POrRieRtu", port=22)
        print("connection established")
    except Exception as e:
        print("connection failed")

    request.cls.client = client

    yield

    client.close()






@pytest.fixture(scope="class")
def setup_webem(request):
    nb_of_resets = int(input("Enter number of resets you want to perform:"))
    test_line_link = input("Please provide your test line link :")

    driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    driver.get(test_line_link)
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


    button3 = driver.find_element_by_xpath('/html/body/div[1]/div/div/ui-modal-renderer/login-banner-modal/ui-modal/div/div/div[3]/div/ui-footer/div/ui-button[1]/button')
    button3.click()

    request.cls.driver = driver
    request.cls.nb_of_resets = nb_of_resets
    yield
    driver.close()






