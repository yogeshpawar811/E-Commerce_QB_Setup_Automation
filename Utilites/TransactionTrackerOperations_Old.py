'''

@ Author - Yogesh Pawar
@ Creation date - 09/21/2018
@ Description - Common Transaction Tracker Operation
'''

from Utilites import AppConstants
from Utilites.SeleniumOperations import SeleniumOperations
from Utilites.LogFileUtility import LogFileUtility
from Utilites.ExcelOperations import ExcelOperations
from Applications.Workflows.ProductionDataMonitoring.AppResources import LocalElementLocator
import time
import openpyxl
from selenium.common.exceptions import NoSuchElementException
import re

class TransactionTrackerOperations:
    def __init__(self, task_type, driver, lo):
        self.v_input_wb = openpyxl.load_workbook(AppConstants.INPUT_FILE_PATH)
        self.v_task_type = task_type
        self.v_input_sheet = self.v_input_wb.get_sheet_by_name("CreditMemoInputData")
        self.driver = driver
        self.lo = lo


    def select_customer(self, customer_type, customer_name):
        self.lo.log_to_file("INFO", "Executing method 'select_customer' from TransactionTrackerOperations")
        so = SeleniumOperations(self.v_task_type, self.driver, self.lo)
        print("Search for: " + str(customer_name))
        time.sleep(2)
        if customer_type == "Company":
            time.sleep(1)

            self.driver.find_element_by_xpath(LocalElementLocator.COMPANY_SEARCH_INPUTBOX).send_keys(customer_name)
        if customer_type == "Trading Partner":
            TP_name = self.driver.find_element_by_xpath(LocalElementLocator.TRADING_SEARCH_INPUTBOX)
            time.sleep(2)
            TP_name.send_keys(customer_name)
        time.sleep(2)
        count = self.driver.find_elements_by_xpath(".//*[contains(@id,'ui-select-choices-row-')]")
        for i in range(len(count)):
            if customer_type == "Company":
                customer_from_TT = self.driver.find_element_by_xpath(
                    ".//*[@id='ui-select-choices-row-1-" + str(i) + "']/div/div").text
            if customer_type == "Trading Partner":
                customer_from_TT = self.driver.find_element_by_xpath(
                    ".//*[@id='ui-select-choices-row-2-" + str(i) + "']/div/div").text
            if customer_name.lower() == customer_from_TT.lower():
                if customer_type == "Company":
                    self.driver.find_element_by_xpath(".//*[@id='ui-select-choices-row-1-" + str(i) + "']/div/div").click()
                if customer_type == "Trading Partner":
                    self.driver.find_element_by_xpath(".//*[@id='ui-select-choices-row-2-" + str(i) + "']/div/div").click()
                print("Found matching customer name at position: " + str(i + 1))
                break
        time.sleep(2)


    def get_CM_parcels(self,input_sheet,row):
        time.sleep(2)
        whilevalue=1
        while(whilevalue):
            try:
                so = SeleniumOperations(self.v_task_type, self.driver, self.lo)
                eo = ExcelOperations(self.v_task_type, input_sheet)
                error_parcel_comment = ''
                without_error_parcel_comment = ''
                without_error_parcel_count = 0
                error_parcel_count = 0
                j = 1
                while (1):
                    i = 1
                    parcel_id = self.driver.find_element_by_xpath(
                        ".//*[@id='parentTablesContainer']/div[1]/table/tbody/tr[" + str(i) + "]/td[2]")
                    while (parcel_id.is_enabled()):
                        try:
                            parcel_id1 = self.driver.find_element_by_xpath(
                                ".//*[@id='parentTablesContainer']/div[1]/table/tbody/tr[" + str(i) + "]/td[2]").text
                        except NoSuchElementException:
                            break

                        status = self.driver.find_element_by_xpath(
                            ".//*[@id='parentTablesContainer']/div[2]/table/tbody/tr[" + str(i) + "]/td[1]").text
                        document_id = self.driver.find_element_by_xpath(
                            ".//*[@id='parentTablesContainer']/div[2]/table/tbody/tr[" + str(i) + "]/td[5]").text
                        if "CM" in document_id:
                            if "Completed w/o Errors" in status:
                                # print("---------------No Errors Data--------------")
                                without_error_parcel_count = without_error_parcel_count + 1
                                without_error_parcel_comment = without_error_parcel_comment + str(
                                    without_error_parcel_count) + ") Parcel ID: " + str(parcel_id1) + " (Document ID: " + str(
                                    document_id) + ") with status: " + str(status) + "\n"
                            if "Completed w/Errors" in status:
                                # print("---------------Errors Data--------------")
                                error_parcel_count = error_parcel_count + 1
                                error_parcel_comment = error_parcel_comment + str(error_parcel_count) + ") Parcel ID: " + str(
                                    parcel_id1) + " (Document ID: " + str(document_id) + ") with status: " + str(status)
                                # print(error_parcel_comment)
                        i = i + 1
                        j = j + 1
                        try:
                            parcel_id = self.driver.find_element_by_xpath(
                                ".//*[@id='parentTablesContainer']/div[1]/table/tbody/tr[" + str(i) + "]/td[2]")
                        except NoSuchElementException:
                            # j = j + 10
                            print("No element found")

                    checkButton = self.driver.find_element_by_xpath(
                        "html/body/app-reporting/div/div/div/div/div/section/div[3]/form/div/button[2]")
                    if (checkButton.is_enabled()):
                        checkButton = self.driver.find_element_by_xpath(
                            "html/body/app-reporting/div/div/div/div/div/section/div[3]/form/div/button[2]")
                        checkButton.click()
                        time.sleep(2)

                    else:
                        print("---------------No Errors Data--------------")
                        print(without_error_parcel_comment)
                        print("----------------Errors Data----------------")
                        print(error_parcel_comment)
                        eo.set_value(row, 6, without_error_parcel_count)
                        eo.set_value(row, 7, without_error_parcel_comment)
                        eo.set_value(row, 8, error_parcel_comment)
                        self.driver.get(LocalElementLocator.TRANSACTION_TRACKER_PROD_LINK)
                        time.sleep(4)
                        break
            except NoSuchElementException:
                # print("No data for this connection")
                break
        try:
            parcel_id1 = self.driver.find_element_by_xpath(
            ".//*[@id='parentTablesContainer']/div[1]/table/tbody/tr[1]/td[2]").text
        except NoSuchElementException:
            self.driver.get(LocalElementLocator.TRANSACTION_TRACKER_PROD_LINK)
            whilevalue==0
            time.sleep(2)








        # Methode for execute search process for Premier Credit Memo PDM task

    def get_all_parcels(self, input_sheet, row):
        time.sleep(2)
        whilevalue = 1
        while (whilevalue):
            try:
                so = SeleniumOperations(self.v_task_type, self.driver, self.lo)
                eo = ExcelOperations(self.v_task_type, input_sheet)
                error_parcel_comment = ''
                without_error_parcel_comment = ''
                without_error_parcel_count = 0
                error_parcel_count = 0
                j = 1
                while (1):
                    i = 1
                    parcel_id = self.driver.find_element_by_xpath(
                        ".//*[@id='parentTablesContainer']/div[1]/table/tbody/tr[" + str(i) + "]/td[2]")
                    while (parcel_id.is_enabled()):
                        try:
                            parcel_id1 = self.driver.find_element_by_xpath(
                                ".//*[@id='parentTablesContainer']/div[1]/table/tbody/tr[" + str(i) + "]/td[2]").text
                        except NoSuchElementException:
                            break

                        status = self.driver.find_element_by_xpath(
                            ".//*[@id='parentTablesContainer']/div[2]/table/tbody/tr[" + str(i) + "]/td[1]").text
                        document_id = self.driver.find_element_by_xpath(
                            ".//*[@id='parentTablesContainer']/div[2]/table/tbody/tr[" + str(i) + "]/td[5]").text
                        if "Completed w/o Errors" in status:
                            # print("---------------No Errors Data--------------")
                            without_error_parcel_count = without_error_parcel_count + 1
                            without_error_parcel_comment = without_error_parcel_comment + str(
                                without_error_parcel_count) + ") Parcel ID: " + str(
                                parcel_id1) + " (Document ID: " + str(
                                document_id) + ") with status: " + str(status) + "\n"
                        if "Completed w/Errors" in status:
                            # print("---------------Errors Data--------------")
                            error_parcel_count = error_parcel_count + 1
                            error_parcel_comment = error_parcel_comment + str(
                                error_parcel_count) + ") Parcel ID: " + str(
                                parcel_id1) + " (Document ID: " + str(document_id) + ") with status: " + str(status)
                        i = i + 1
                        j = j + 1
                        try:
                            parcel_id = self.driver.find_element_by_xpath(
                                ".//*[@id='parentTablesContainer']/div[1]/table/tbody/tr[" + str(i) + "]/td[2]")
                        except NoSuchElementException:
                            print("No element found")

                    checkButton = self.driver.find_element_by_xpath(
                        "html/body/app-reporting/div/div/div/div/div/section/div[3]/form/div/button[2]")
                    if (checkButton.is_enabled()):
                        checkButton = self.driver.find_element_by_xpath(
                            "html/body/app-reporting/div/div/div/div/div/section/div[3]/form/div/button[2]")
                        checkButton.click()
                        time.sleep(2)

                    else:
                        print("---------------No Errors Data--------------")
                        print(without_error_parcel_comment)
                        print("----------------Errors Data----------------")
                        print(error_parcel_comment)
                        eo.set_value(row, 6, without_error_parcel_count)
                        eo.set_value(row, 7, without_error_parcel_comment)
                        eo.set_value(row, 8, error_parcel_comment)
                        self.driver.get(LocalElementLocator.TRANSACTION_TRACKER_PROD_LINK)
                        time.sleep(4)
                        break
            except NoSuchElementException:
                # print("No data for this connection")
                break
        try:
            parcel_id1 = self.driver.find_element_by_xpath(
                ".//*[@id='parentTablesContainer']/div[1]/table/tbody/tr[1]/td[2]").text
        except NoSuchElementException:
            self.driver.get(LocalElementLocator.TRANSACTION_TRACKER_PROD_LINK)
            whilevalue == 0
            time.sleep(2)

        # Methode for execute search process for Premier Credit Memo PDM task

    def search_process_for_CMPDM(self,supplier,retailer,doc_type,date, input_sheet,row):

        print("=====================================Task Number: "+str(row-1)+"===================================")
        print("============================================================================================")
        self.lo.log_to_file("INFO", "Executing method 'search_process' from TransactionTrackerOperations")
        self.driver.switch_to.frame(0)
        so = SeleniumOperations(self.v_task_type, self.driver, self.lo)
        time.sleep(2)
        self.select_customer("Company",supplier)
        time.sleep(1)
        self.select_customer("Trading Partner",retailer)
        so.send_text_by_xpath(LocalElementLocator.START_DATE,date)
        so.click_element_by_xpath(LocalElementLocator.SERVICE)
        so.click_element_by_xpath(LocalElementLocator.DC4ROUTER)
        so.send_text_by_xpath(LocalElementLocator.DOCUMENT_TYPE,doc_type)
        so.click_element_by_xpath(LocalElementLocator.SEARCH_BTN)
        time.sleep(3)
        self.get_CM_parcels(input_sheet, row)
        time.sleep(2)

    def search_process_for_PDM(self,supplier,retailer,doc_type,date, input_sheet,row):

        print("=====================================Task Number: "+str(row-1)+"===================================")
        print("============================================================================================")
        self.lo.log_to_file("INFO", "Executing method 'search_process' from TransactionTrackerOperations")
        self.driver.switch_to.frame(0)
        so = SeleniumOperations(self.v_task_type, self.driver, self.lo)
        time.sleep(2)
        self.select_customer("Company",supplier)
        time.sleep(1)
        self.select_customer("Trading Partner",retailer)
        so.send_text_by_xpath(LocalElementLocator.START_DATE,date)
        so.click_element_by_xpath(LocalElementLocator.SERVICE)
        so.click_element_by_xpath(LocalElementLocator.DC4ROUTER)
        so.send_text_by_xpath(LocalElementLocator.DOCUMENT_TYPE,doc_type)
        so.click_element_by_xpath(LocalElementLocator.SEARCH_BTN)
        time.sleep(3)
        self.get_all_parcels(input_sheet, row)
        time.sleep(2)


