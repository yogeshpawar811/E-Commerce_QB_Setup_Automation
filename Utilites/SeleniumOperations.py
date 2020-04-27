'''

@ Author - Karan Pandya
@ Creation date - 08/27/2018
@ Description - Wraper class for selenium methods.
# If element is not found, the method return false to be handled in the main class file.
'''

from selenium import webdriver
from Utilites import AppConstants
from Utilites.LogFileUtility import LogFileUtility
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class SeleniumOperations:

    def __init__(self, v_task_type, driver, lo):
        self.driver = driver
        self.task_type = v_task_type
        self.lo = lo
    def explicit_wait(self, v_element_id, v_element_id_type):
        if v_element_id_type == "BY_ID":
            try:
                element = WebDriverWait(self.driver, 50).until(
                    EC.presence_of_element_located((By.ID, v_element_id))
                )
            except NoSuchElementException:
                self.lo.log_to_file("ERROR", "Error in SeleniumOperations.Explicit_wait(). Element not found for id")

                return False
            return True

        if v_element_id_type == "BY_XPATH":
            try:
                element = WebDriverWait(self.driver, 50).until(
                    EC.presence_of_element_located((By.XPATH, v_element_id))
                )
            except NoSuchElementException:
                self.lo.log_to_file("ERROR", "Error in SeleniumOperations.Explicit_wait(). Element not found for XPATH")

                return False
            return True

        if v_element_id_type == "BY_NAME":
            try:
                element = WebDriverWait(self.driver, 50).until(
                    EC.presence_of_element_located((By.NAME, v_element_id))
                )
            except NoSuchElementException:
                self.lo.log_to_file("ERROR", "Error in SeleniumOperations.Explicit_wait(). Element not found for NAME")

                return False
            return True



    def send_text_by_id(self, v_element_id, v_text_value):

        if self.explicit_wait(v_element_id, 'BY_ID'):
            self.driver.find_element_by_id(v_element_id).clear()
            self.driver.find_element_by_id(v_element_id).send_keys(v_text_value)
        else:
            self.lo.log_to_file("ERROR", "Error in SeleniumOperations.send_text(). Element not found for id")
            return False

    def send_text_by_xpath(self, v_element_id, v_text_value):

        if self.explicit_wait(v_element_id, 'BY_XPATH'):
            self.driver.find_element_by_xpath(v_element_id).clear()
            self.driver.find_element_by_xpath(v_element_id).send_keys(v_text_value)
        else:
            self.lo.log_to_file("ERROR", "Error in SeleniumOperations.send_text(). Element not found for id")
            return False

    def send_text_by_name(self, v_element_id, v_text_value):

        if self.explicit_wait(v_element_id, 'BY_NAME'):
            self.driver.find_element_by_name(v_element_id).clear()
            self.driver.find_element_by_name(v_element_id).send_keys(v_text_value)
        else:
            self.lo.log_to_file("ERROR", "Error in SeleniumOperations.send_text(). Element not found for id")
            return False


    def click_element_by_id(self, v_element_id):

        if self.explicit_wait(v_element_id, 'BY_ID'):
            self.driver.find_element_by_id(v_element_id).click()
        else:
            self.lo.log_to_file("ERROR", "Error in SeleniumOperations.Click(). Element not found for Id")
            return False

    def click_element_by_xpath(self, v_element_id):

        if self.explicit_wait(v_element_id, 'BY_XPATH'):
            self.driver.find_element_by_xpath(v_element_id).click()
        else:
            self.lo.log_to_file("ERROR", "Error in SeleniumOperations.Click(). Element not found for Id")
            return False

    def click_element_by_name(self, v_element_id):

        if self.explicit_wait(v_element_id, 'BY_NAME'):
            self.driver.find_element_by_name(v_element_id).click()
        else:
            self.lo.log_to_file("ERROR", "Error in SeleniumOperations.Click(). Element not found for Id")
            return False



    def get_text_by_id(self, v_element_id):

        if self.explicit_wait(v_element_id, 'BY_ID'):
            result = self.driver.find_element_by_id(v_element_id).text
            return result
        else:
            self.lo.log_to_file("ERROR", "Error in SeleniumOperations.text(). Element not found for Id")
            return False

    def get_text_by_xpath(self, v_element_id):

        if self.explicit_wait(v_element_id, 'BY_XPATH'):
            result = self.driver.find_element_by_xpath(v_element_id).text
            return result
        else:
            self.lo.log_to_file("ERROR", "Error in SeleniumOperations.text(). Element not found for Id")
            return False

    def get_text_by_name(self, v_element_id):

        if self.explicit_wait(v_element_id, 'BY_NAME'):
            result = self.driver.find_element_by_name(v_element_id).text
            return result
        else:
            self.lo.log_to_file("ERROR", "Error in SeleniumOperations.text(). Element not found for Id")
            return False

    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def check_exists_by_name(self, name):
        try:
            self.driver.find_element_by_name(name)
        except NoSuchElementException:
            return False
        return True

    def check_exists_by_id(self, id):
        try:
            self.driver.find_element_by_id(id)
        except NoSuchElementException:
            return False
        return True

    def check_clickable_by_xpath(self, v_element_id):
        try:
            self.driver.find_element_by_xpath(v_element_id).click()
            # SeleniumOperations.click_element_by_xpath(v_element_id)
        except NoSuchElementException:
            return False
        return True



