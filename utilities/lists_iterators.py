from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

# from utilities.xpaths import 
from utilities.css_selector import list_of_people_selector, popup_connect
from utilities.classes import list_of_people_class, navigation_bar

def list_of_people(driver, iterations=1, delay=0):
    """
    """

    for i in range(iterations):
        _css_selector = list_of_people_selector
        webelement = WebDriverWait(driver, 5).until(EC.presence_of_element_located((\
            By.CSS_SELECTOR, _css_selector )))
        options = webelement.find_elements_by_tag_name("li")
        
        for elem in options:
            for item in elem.find_elements_by_class_name("artdeco-button__text"):
                if str(item.text).strip() == "Conectar" or str(item.text).strip() == "Connects":
                    item.click()
                    sleep(1)
                    popup = driver.find_elements_by_css_selector(popup_connect)
                    popup = popup[0]
                    for popupitem in popup.find_elements_by_class_name("artdeco-button__text"):
                        if str(popupitem.text).strip() == "Enviar" or str(popupitem.text).strip() == "Send":
                            popupitem.click()
                            sleep(1)

        sleep(5)
        # scroll down
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        _css_selector = "[class$='%s']"%navigation_bar
        nav_bar = WebDriverWait(driver, 5).until(EC.presence_of_element_located((\
            By.CSS_SELECTOR, _css_selector )))
        for item in nav_bar.find_elements_by_class_name("artdeco-button__text"):
            if str(item.text).strip() == "Siguiente" or str(item.text).strip() == "Next":
                # print(item.text)
                item.click()
            break

        sleep(2)

    sleep(delay)