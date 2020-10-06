import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from TestData.UserData import testUserData
import time
from selenium import webdriver
import os.path
from Utilities.BaseClass import BaseClass
from TestData.SwData import SwData

from pathlib import Path

import webbrowser
import pytest


class TestSw(SwData) :

    def test_sw_download(self, getUserData):

        sw_name = str(input("Please enter the name of the build to download :"))

        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        self.driver.get(self.getswdata(sw_name))

        self.driver.maximize_window()

        username = self.driver.find_element_by_name("USER")
        username.send_keys(getUserData["login"])
        password = self.driver.find_element_by_name("PASSWORD")
        password.send_keys(getUserData["password"])

        submit = self.driver.find_element_by_id("submit")
        submit.click()

        time.sleep(5)

        title = self.driver.find_element_by_id("page-title").text
        print(title)

        reference = title[-4:]
        reference2 = " "
        download = self.driver.find_element_by_xpath("//a[@id='ui-id-8']")
        download.click()

        time.sleep(15)

        sw = self.driver.find_elements_by_partial_link_text("AirScale-0.800." + reference + "_")

        for elem in sw:
            if "ASIB_ABIO" in elem.text:
                elem.click()
                reference2 = elem.text

        print(reference2)

        f = "C:/Users/tlazaar/Downloads/" + reference2

        while not os.path.exists(f):
            time.sleep(1)

        if os.path.isfile(f):
            print("file is downloaded")
        else:
            print("download failed")

    @pytest.fixture(params=testUserData.test_userData)
    def getUserData(self, request):
        return request.param
