from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import logging
from Page_Objects import HomePage

logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("setup_webem")
def test_gNb_reset(setup_webem):

    logger.info("info")
    logger.debug("debug")
    logger.warning("warning")
    logger.error("errors")
    logger.critical("critical")


    reset = WebDriverWait(setup_webem, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-view"]/div/div[1]/div[2]/ng-view/wf-panel/wf-panel-section/div/div/site-runtime-views/div/div/div[1]/simplified-site-tab/toolbar/execution-bar/div/reset-site-button/div/ui-button/button')))
    reset.click()

    time.sleep(5)
    reset2 = setup_webem.find_element_by_css_selector('body > div.modal.reset-site-operations.ng-scope.ng-isolate-scope.in > div > div > common-modal > div > div > div.modal-footer > div > modal-footer > ui-button:nth-child(1) > button')
    reset2.click()

    closewindow = WebDriverWait(setup_webem, 180).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/ui-modal-renderer/bts-status-modal/ui-modal/div/div/div[3]/div/ui-footer/div/ui-button/button')))
    closewindow.click()

    time.sleep(360)

    message = setup_webem.find_element_by_xpath('//*[@id="main-view"]/div/div[1]/div[1]/div/div[2]/cells-delivery/cells-status/div/div[1]').text
    print(message)

    assert "air" in message , "cell setup failed"


