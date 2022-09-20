#!/usr/bin/env python3
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
# secure imports
import configparser
# import utilities
from utilities.buttons import select_job_filter, select_people_filter
from utilities.text_boxes import login_by_xpath, \
    search_specific_subject
from utilities.lists_iterators import list_of_people
from utilities.xpaths import login_name, login_pass

def create_driver_session(session_id, executor_url):
    from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

    # Save the original function, so we can revert our patch
    org_command_execute = RemoteWebDriver.execute

    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return org_command_execute(self, command, params)

    # Patch the function before creating the driver object
    RemoteWebDriver.execute = new_command_execute

    new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    new_driver.session_id = session_id

    # Replace the patched function with original function
    RemoteWebDriver.execute = org_command_execute

    return new_driver

def get_url(driver, url, delay=0):
    driver.get(url)
    sleep(delay)

def login(driver, name_xpath, pass_xpath, name, password):
    """
    """
    TIME_WAIT = 3
    sleep(TIME_WAIT)
    login_by_xpath(driver, name_xpath, pass_xpath, name, password)
    sleep(TIME_WAIT)

def close_father_webdriver(driver):
    driver.close() # better just press ENTER at the main bash

def main():
    config = configparser.ConfigParser()
    config.read("config/session/session.ini")
    session_id =  config['SESSION']['session_id']
    executor_url = config['SESSION']['executor_url']
    driver = create_driver_session(session_id, executor_url)
    # read credentials
    config.read("config/session/credentials.ini")
    name =  config['LOGIN']['name']
    password = config['LOGIN']['password']

    from messages import messages

    ## ------------ close webdriver # UNCOMMENT ONLY IF NEEDED!!!!
    # close_father_webdriver(driver)

    # get the home page
    base_url = 'https://www.linkedin.com/'
    get_url(driver, base_url, delay=5)

    ## ----------- login
    login(driver, login_name, login_pass, name, password)

    subject = raw_input("\n---> Introduce a subject (default='computer visions'): ")
    subject = "computer vision" if subject == "" else subject

    ## ----------- select subject
    search_specific_subject(driver, subject=subject)

    ## ----------- select people filter button
    select_people_filter(driver, delay=0)

    ## ----------- iterate over people
    list_of_people(driver, iterations=50, delay=5)

    sleep(10)
    driver.get('https://www.duckduckgo.com')
    # close_father_webdriver(driver)

if __name__ == "__main__":
    main()