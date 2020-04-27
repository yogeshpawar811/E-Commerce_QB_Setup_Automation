'''
@ Author - Yogesh Pawar
@ Creation date - 01/13/2020
@ Description - TransactionTrackerActions
'''

import time
import pyperclip
import openpyxl
from Utilites.Login import Login
from Utilites import AppConstants
from selenium import webdriver
# from Applications.Workflows.ServiceTimeCard.RPA.AppResources import ElementLocators
from Applications.Workflows.ProductionDataMonitoring.AppResources import LocalElementLocator
from Applications.Workflows.ProductionDataMonitoring.Scripts.ProductionDataMonitoring_TransactionTrackerOperations import TransactionTrackerOperations
from Utilites.SeleniumOperations import SeleniumOperations
from Applications.Workflows.ServiceTimeCard.DocumentProcessing.AppResources import ElementLocators
import select



class TransactionTrackerActions:
    def __init__(self, task_type, lo, username):
        self.v_input_wb = openpyxl.load_workbook(ElementLocators.INPUT_FILE_PATH)
        self.v_task_type = task_type
        self.v_input_sheet = self.v_input_wb.get_sheet_by_name("Input")
        self.log = lo
        self.v_username = username


    def Login_Launchpad(self,driver):
        so = SeleniumOperations(self.v_task_type, driver, self.log)
        driver.get(ElementLocators.TRANSACTION_TRACKER_PROD_LINK)
        time.sleep(7)
        driver.switch_to.frame(0)
        # driver.find_element_by_xpath(ElementLocators.tt_username).send_keys(ElementLocators.tt_uname)
        # time.sleep(5)
        so.send_text_by_xpath(ElementLocators.tt_username, ElementLocators.tt_uname)
        so.send_text_by_xpath(ElementLocators.tt_password, ElementLocators.tt_pw)
        so.click_element_by_xpath(ElementLocators.tt_login_btn)
        time.sleep(2)

    def Generate_TT_Prod_URL(error_parcel_id):
        URL="https://commerce.spscommerce.com/transaction-tracker/prod/transactions/"+str(error_parcel_id)+"/"
        return URL


    def get_parcels_errors(driver):
        # so = SeleniumOperations(self.v_task_type, driver, self.log)
        errors_list=''
        time.sleep(7)
        errors = driver.find_elements_by_xpath(".//*[@class='error-description']")
        for ii in errors:
            print("==================================================")
            print(ii.text)
            errors_list = errors_list + ii.text + "\n"
        print(errors_list)
        return errors_list


    def save_errors_in_excel(self,row,errors_list):
        self.v_input_sheet.cell(row=row, column=3).value = errors_list
        self.v_input_wb.save(ElementLocators.INPUT_FILE_PATH)

    def for_unpo(self, driver, profile_uid):
        so = SeleniumOperations(self.v_task_type, driver, self.log)
        driver.get("https://commerce.spscommerce.com/migrator/")
        time.sleep(10)
        driver.switch_to.frame(0)
        time.sleep(5)
        driver.find_element_by_xpath(".//*[contains(text(),'Search by column')]//select").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[contains(text(),'profile_uid')]").click()
        # time.sleep(3)
        # driver.find_element_by_xpath(".//b").click()
        time.sleep(4)
        driver.find_element_by_xpath("html/body/div[1]/div/div/api-interaction/div/div[4]/label/chosen-select/div/a").click()
        time.sleep(4)
        driver.find_element_by_xpath("html/body/div[1]/div/div/api-interaction/div/div[4]/label/chosen-select/div/div/div/input").send_keys(profile_uid)
        # driver.find_element_by_xpath("html/body/div[1]/div/div/api-interaction/div/div[4]/label/chosen-select/div/div/div/input").click()
        time.sleep(3)
        driver.find_element_by_xpath("html/body/div[1]/div/div/api-interaction/div/div[4]/label/chosen-select/div/div/div/input").clear()
        driver.find_element_by_xpath("html/body/div[1]/div/div/api-interaction/div/div[4]/label/chosen-select/div/div/div/input").send_keys(profile_uid)
        time.sleep(3)
        driver.find_element_by_xpath(".//ul/li").click()
        time.sleep(2)

        # driver.find_element_by_xpath("html/body/div[1]/div/div/api-interaction/div/div[4]/label/chosen-select/div/div/div/input").click()

        # time.sleep(3)

        pyperclip.copy(profile_uid)
        # self.v_driver.find_element_by_xpath(".//*[@class='chosen-search-input']")
        print("======================================")
        # print(pf_id)
        pyperclip.paste()



        # driver.find_element_by_xpath(".//li[1]").click()
        time.sleep(15)
