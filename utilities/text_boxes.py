from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from lxml import etree
from time import sleep

from utilities.xpaths import login_name, login_pass, \
    search_box_home_xpath
from utilities.classes import search_box_home_class

def login_by_xpath(driver, name_xpath, pass_xpath, name, password):
    # find name textbox
    textbox = WebDriverWait(driver, 5).until(EC.presence_of_element_located((\
        By.XPATH, name_xpath )))
    textbox.click()
    textbox.send_keys( name )

    # find password textbox
    textbox = WebDriverWait(driver, 5).until(EC.presence_of_element_located((\
        By.XPATH, pass_xpath )))
    textbox.click()
    textbox.send_keys( password )

    textbox.send_keys(Keys.ENTER)
    return 0

def search_specific_subject(driver, subject, delay=0):
    """
    Search specific subject on search textbox
    """
    # select textbox and send keys
    _key = subject
    _css_selector = "[class$='%s']"%search_box_home_class
    # webelement = WebDriverWait(driver, 5).until(EC.presence_of_element_located((\
        # By.XPATH, _xpath )))
    webelement = WebDriverWait(driver, 5).until(EC.presence_of_element_located((\
        By.CSS_SELECTOR, _css_selector )))
    webelement.click()
    webelement.send_keys( subject )
    sleep(1)
    webelement.send_keys(Keys.ENTER)

    sleep(delay)


    