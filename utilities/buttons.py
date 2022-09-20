from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

from utilities.css_selector import job_filter_button, people_filter_button

def select_job_filter(driver, delay=0):
    """
    """
    _css_selector = job_filter_button
    # webelement = WebDriverWait(driver, 5).until(EC.presence_of_element_located((\
        # By.XPATH, _xpath )))
    webelement = WebDriverWait(driver, 5).until(EC.presence_of_element_located((\
        By.CSS_SELECTOR, _css_selector )))
    webelement.click()

    sleep(delay)


def select_people_filter(driver, delay=0):
    """
    """
    _css_selector = people_filter_button
    # webelement = WebDriverWait(driver, 5).until(EC.presence_of_element_located((\
        # By.XPATH, _xpath )))
    webelement = WebDriverWait(driver, 5).until(EC.presence_of_element_located((\
        By.CSS_SELECTOR, _css_selector )))
    webelement.click()

    sleep(delay)