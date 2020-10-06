import logging
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

from Utilities.BaseClass import BaseClass
from Page_Objects.HomePage import WebEm

logger = logging.getLogger(__name__)




class TestgNBreset(BaseClass):
    def test_gNbreset(self):

        reset_failed = 0
        reset_success = 0

        for i in range (self.nb_of_resets) :

            self.driver.implicitly_wait(180)

            logger.info("info")
            logger.debug("debug")
            logger.warning("warning")
            logger.error("errors")
            logger.critical("critical")

            webem = WebEm(self.driver)

            try:

               webem.Closewindow_1().click()

            except NoSuchElementException:

                continue

            webem.Reset().click()

            webem.ConfirmReset().click()

            webem.Closewindow().click()

            time.sleep(360)

            cell_status = webem.getMessage().text

            print(cell_status)

            if cell_status != "On air":
                self.snapshotcollect()
                self.driver.back()
                reset_failed += 1
                print("reset failed")
            else:
                reset_success += 1
                print("successful reset")


