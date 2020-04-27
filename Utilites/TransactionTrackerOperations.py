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
from selenium import webdriver
from Utilites.LogFileUtility import LogFileUtility
import re

class TransactionTrackerOperations:
    def __init__(self, task_type, driver, lo):
        self.v_input_wb = openpyxl.load_workbook(AppConstants.INPUT_FILE_PATH)
        self.v_task_type = task_type
        self.v_input_sheet = self.v_input_wb.get_sheet_by_name("CreditMemoInputData")
        self.driver = driver
        self.lo = lo


    # generic method for search supplier and retailer in TT
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
        count = self.driver.find_elements_by_xpath(LocalElementLocator.DROP_DOWN_LIST)
        for i in range(len(count)):
            if customer_type == "Company":
                customer_from_TT = self.driver.find_element_by_xpath(
                    LocalElementLocator.CUSTOMER_FROM_TT_FOR_COMPANY_1 + str(
                        i) + LocalElementLocator.CUSTOMER_FROM_TT_FOR_COMPANY_2).text
            if customer_type == "Trading Partner":
                customer_from_TT = self.driver.find_element_by_xpath(
                    LocalElementLocator.CUSTOMER_FROM_TT_FOR_TRADING_PARTNER_1 + str(
                        i) + LocalElementLocator.CUSTOMER_FROM_TT_FOR_TRADING_PARTNER_2).text
            if customer_name.lower() == customer_from_TT.lower():
                if customer_type == "Company":
                    self.driver.find_element_by_xpath(LocalElementLocator.CUSTOMER_FROM_TT_FOR_COMPANY_1+ str(i) + LocalElementLocator.CUSTOMER_FROM_TT_FOR_COMPANY_2).click()
                if customer_type == "Trading Partner":
                    self.driver.find_element_by_xpath(LocalElementLocator.CUSTOMER_FROM_TT_FOR_TRADING_PARTNER_1 + str(i) + LocalElementLocator.CUSTOMER_FROM_TT_FOR_TRADING_PARTNER_2).click()
                print("Found matching customer name at position: " + str(i + 1))
                break
        time.sleep(2)

    # method for get Credit Memo parcels
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
                    parcel_id = self.driver.find_element_by_xpath(LocalElementLocator.PARCEL_ID_1 + str(i) + LocalElementLocator.PARCEL_ID_2)
                    while (parcel_id.is_enabled()):
                        try:
                            parcel_id1 = self.driver.find_element_by_xpath(LocalElementLocator.PARCEL_ID_1 + str(i) + LocalElementLocator.PARCEL_ID_2).text
                        except NoSuchElementException:
                            break

                        status = self.driver.find_element_by_xpath(LocalElementLocator.STATUS_1 + str(i) + LocalElementLocator.STATUS_2).text
                        document_id = self.driver.find_element_by_xpath(LocalElementLocator.DOCUMENT_ID_1 + str(i) + LocalElementLocator.DOCUMENT_ID_2).text
                        if "CM" in document_id:
                            if "Completed w/o Errors" in status:
                                without_error_parcel_count = without_error_parcel_count + 1
                                without_error_parcel_comment = without_error_parcel_comment + str(
                                    without_error_parcel_count) + ") Parcel ID: " + str(parcel_id1) + " (Document ID: " + str(
                                    document_id) + ") with status: " + str(status) + "\n"
                            if "Completed w/Errors" in status:
                                error_parcel_count = error_parcel_count + 1
                                error_parcel_comment = error_parcel_comment + str(error_parcel_count) + ") Parcel ID: " + str(
                                    parcel_id1) + " (Document ID: " + str(document_id) + ") with status: " + str(status)
                        i = i + 1
                        j = j + 1
                        try:
                            parcel_id = self.driver.find_element_by_xpath(LocalElementLocator.PARCEL_ID_1 + str(i) + LocalElementLocator.PARCEL_ID_2)
                        except NoSuchElementException:
                            print("No element found")

                    next_button = self.driver.find_element_by_xpath(LocalElementLocator.NEXT_SEARCH_BTN)

                    if (next_button.is_enabled()):
                        next_button = self.driver.find_element_by_xpath(LocalElementLocator.NEXT_SEARCH_BTN)
                        next_button.click()
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
                break
        try:
            parcel_id1 = self.driver.find_element_by_xpath(LocalElementLocator.LAST_PARCEL_ID).text
        except NoSuchElementException:
            self.driver.get(LocalElementLocator.TRANSACTION_TRACKER_PROD_LINK)
            whilevalue==0
            time.sleep(2)








        # Methode for execute search process for Premier Credit Memo PDM task

    # method for get all parcels
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
                    parcel_id = self.driver.find_element_by_xpath(LocalElementLocator.PARCEL_ID_1 + str(i) + LocalElementLocator.PARCEL_ID_2)
                    while (parcel_id.is_enabled()):
                        try:
                            parcel_id1 = self.driver.find_element_by_xpath(LocalElementLocator.PARCEL_ID_1 + str(i) + LocalElementLocator.PARCEL_ID_2).text
                        except NoSuchElementException:
                            break

                        status = self.driver.find_element_by_xpath(LocalElementLocator.STATUS_1 + str(i) + LocalElementLocator.STATUS_2).text
                        document_id = self.driver.find_element_by_xpath(LocalElementLocator.DOCUMENT_ID_1 + str(i) + LocalElementLocator.DOCUMENT_ID_2).text
                        if "Completed w/o Errors" in status:
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
                            parcel_id = self.driver.find_element_by_xpath(LocalElementLocator.PARCEL_ID_1 + str(i) + LocalElementLocator.PARCEL_ID_2)
                        except NoSuchElementException:
                            print("No element found")

                    next_button = self.driver.find_element_by_xpath(LocalElementLocator.NEXT_SEARCH_BTN)

                    if (next_button.is_enabled()):
                        next_button = self.driver.find_element_by_xpath(LocalElementLocator.NEXT_SEARCH_BTN)
                        next_button.click()
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
                break
        try:
            parcel_id1 = self.driver.find_element_by_xpath(LocalElementLocator.LAST_PARCEL_ID).text
        except NoSuchElementException:
            self.driver.get(LocalElementLocator.TRANSACTION_TRACKER_PROD_LINK)
            whilevalue==0
            time.sleep(2)

        # Methode for execute search process for Premier Credit Memo PDM task

    def save_maximum_five_parcels_id(self,parcel_count):
        print("in get_five_parcels method")
        time.sleep(2)
        parcels = ''
        for i in range(parcel_count):
            parcel_id = self.v_driver.find_element_by_xpath(LocalElementLocator.PARCEL_ID_1 + str(i + 1) + LocalElementLocator.PARCEL_ID_2).text
            parcels = parcels + parcel_id + "\n"
        print(parcels)
        file = open(LocalElementLocator.FIRST_FIVE_PARCELS_FILE_PATH, "w+")
        file.write(parcels)

        # Method to create the dynamic path to save the downloaded files

    def create_file_save_path(self, v_supplier, v_retailer):
        self.lo.log_to_file("INFO", "Login in to DC4 Pre_Prod")
        # lg = Login(self.v_task_type, self.v_driver, self.v_input_wb, self.lo)
        # so = SeleniumOperations(self.v_task_type, self.driver, self.lo)
        # eo = ExcelOperations(self.v_task_type, self.v_data_sheet)
        # path1 = '../AppResources/Download Files'
        path = '"download.default_directory=' + '../AppResources/Download Files/' + v_supplier + '_' + v_retailer + '"'
        # path = r'C:\Users\aditya.datar\Downloads'+v_supplier+"_"+v_retailer
        options = webdriver.ChromeOptions()
        options.add_argument(path)
        self.driver = webdriver.Chrome(chrome_options=options)


    def search_by_parcel_id_and_download(self,parcel_id):
        self.create_file_save_path("supplier","retailer")
        print("search_by_parcel_id_and_download method")
        self.driver.get(LocalElementLocator.TRANSACTION_TRACKER_PROD_LINK+parcel_id)
        so = SeleniumOperations(self.v_task_type, self.driver, self.lo)
        time.sleep(1)
        self.driver.switch_to.frame(0)
        time.sleep(1)
        PARCEL_FIRST_STAGE_ID=so.get_text_by_xpath(LocalElementLocator.PARCEL_FIRST_STAGE_ID)
        self.driver.get(LocalElementLocator.TRANSACTION_TRACKER_PROD_LINK+parcel_id+"/parcel/"+PARCEL_FIRST_STAGE_ID)
        time.sleep(2)
        self.driver.switch_to.frame(0)
        so.click_element_by_xpath(LocalElementLocator.DOWNLOAD_LOGO_BUTTON)
        time.sleep(3)


    # method for search data for Credit Memo
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

    # method for search data for all data
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

    # method for search data for all data
    def search_process_for_process_test_file(self,supplier,retailer,doc_type,date):



        print("=====================================Task Number: ===================================")
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
        # self.save_parcels_id_parcels(2)
        # self.search_by_parcel_id_and_download("10944250370")

