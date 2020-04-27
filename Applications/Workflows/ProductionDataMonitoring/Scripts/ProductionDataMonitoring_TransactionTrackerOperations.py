'''

@ Author - Yogesh Pawar
@ Creation date - 09/21/2018
@ Description - Common Transaction Tracker Operation
'''

from Utilites.SeleniumOperations import SeleniumOperations
from Utilites.ExcelOperations import ExcelOperations
import time
from selenium.common.exceptions import NoSuchElementException
from Applications.Workflows.ProductionDataMonitoring.Scripts.ReportFileUtility import ReportFileUtility
from Applications.Workflows.ProductionDataMonitoring.AppResources import LocalElementLocator
from Utilites import AppConstants
import math
import datetime

class TransactionTrackerOperations:
    def __init__(self, task_type, driver, lo,v_input_sheet,v_input_wb,v_username,v_driver):
        self.v_task_type = task_type
        self.driver = driver
        self.log = lo
        self.v_input_sheet=v_input_sheet
        self.v_input_wb=v_input_wb
        self.v_username=v_username
        self.v_driver=v_driver

    # generic method to search supplier and retailer with customer_type as parameter i.e. "Company" OR "Trading Partner"
    def select_customer(self, v_customer_type, v_customer_name):
        self.log.log_to_file("INFO", "Executing TransactionTrackerOperations.select_customer()")
        selenium_operations_object = SeleniumOperations(self.v_task_type, self.driver, self.log)
        time.sleep(2)
        if v_customer_type == "Company":
            selenium_operations_object.send_text_by_xpath(LocalElementLocator.COMPANY_SEARCH_INPUTBOX, v_customer_name)
        if v_customer_type == "Trading Partner":
            selenium_operations_object.send_text_by_xpath(LocalElementLocator.TRADING_SEARCH_INPUTBOX, v_customer_name)
        time.sleep(2)
        count = self.driver.find_elements_by_xpath(LocalElementLocator.DROP_DOWN_LIST)
        for i in range(len(count)):
            if v_customer_type == "Company":
                v_customer_from_TT = selenium_operations_object .get_text_by_xpath(LocalElementLocator.CUSTOMER_FROM_TT_FOR_COMPANY_1 + str(
                    i) + LocalElementLocator.CUSTOMER_FROM_TT_FOR_COMPANY_2)
            if v_customer_type == "Trading Partner":
                v_customer_from_TT = selenium_operations_object .get_text_by_xpath(
                    LocalElementLocator.CUSTOMER_FROM_TT_FOR_TRADING_PARTNER_1 + str(
                        i) + LocalElementLocator.CUSTOMER_FROM_TT_FOR_TRADING_PARTNER_2)
            if v_customer_name.lower() == v_customer_from_TT.lower():
                if v_customer_type == "Company":
                    selenium_operations_object.click_element_by_xpath(LocalElementLocator.CUSTOMER_FROM_TT_FOR_COMPANY_1 + str(
                        i) + LocalElementLocator.CUSTOMER_FROM_TT_FOR_COMPANY_2)
                if v_customer_type == "Trading Partner":
                    selenium_operations_object.click_element_by_xpath(LocalElementLocator.CUSTOMER_FROM_TT_FOR_TRADING_PARTNER_1 + str(
                        i) + LocalElementLocator.CUSTOMER_FROM_TT_FOR_TRADING_PARTNER_2)
                break
        time.sleep(2)


    # method for collect Credit Memo unique parcels and fill input sheet as per result data
    def get_CM_parcels(self,input_sheet,row):
        self.log.log_to_file("INFO", "Executing TransactionTrackerOperations.get_CM_parcels()")
        whilevalue=1
        while(whilevalue):
            try:
                selenium_operations_object = SeleniumOperations(self.v_task_type, self.driver, self.log)
                excel_operations_object = ExcelOperations(self.v_task_type, input_sheet)
                error_parcel_comment = ''
                without_error_parcel_comment = ''
                without_error_parcel_count = 0
                error_parcel_count = 0
                v_start = 1
                while (1):
                    v_second_start = 1
                    parcel_id = self.driver.find_element_by_xpath(LocalElementLocator.PARCEL_ID_1 + str(v_second_start) + LocalElementLocator.PARCEL_ID_2)
                    while (parcel_id.is_enabled()):
                        try:
                            parcel_id1 = self.driver.find_element_by_xpath(LocalElementLocator.PARCEL_ID_1 + str(v_second_start) + LocalElementLocator.PARCEL_ID_2).text
                        except NoSuchElementException:
                            break
                        v_status = selenium_operations_object.get_text_by_xpath(LocalElementLocator.STATUS_1 + str(v_second_start) + LocalElementLocator.STATUS_2)
                        v_document_id = selenium_operations_object.get_text_by_xpath(LocalElementLocator.DOCUMENT_ID_1 + str(v_second_start) + LocalElementLocator.DOCUMENT_ID_2)
                        v_parcel_date_time = selenium_operations_object.get_text_by_xpath(LocalElementLocator.PARCEL_DATE_TIME_1 + str(v_second_start) + LocalElementLocator.PARCEL_DATE_TIME_2)
                        if "CM" in v_document_id:
                            if "Completed w/o Errors" in v_status:
                                without_error_parcel_count = without_error_parcel_count + 1
                                without_error_parcel_comment = without_error_parcel_comment + str(
                                    without_error_parcel_count) + ") Parcel ID: " + str(parcel_id1) + " (Document ID: " + str(
                                    v_document_id) + ") with status: " + str(v_status)+" ["+v_parcel_date_time+"]" + "\n"
                            if "Completed w/Errors" in v_status:
                                error_parcel_count = error_parcel_count + 1
                                error_parcel_comment = error_parcel_comment + str(error_parcel_count) + ") Parcel ID: " + str(
                                    parcel_id1) + " (Document ID: " + str(v_document_id) + ") with status: " + str(v_status)+" ["+v_parcel_date_time+"]" + "\n"
                        v_second_start = v_second_start + 1
                        v_start = v_start + 1
                        try:
                            parcel_id = self.driver.find_element_by_xpath(LocalElementLocator.PARCEL_ID_1 + str(v_second_start) + LocalElementLocator.PARCEL_ID_2)
                        except NoSuchElementException:
                            self.log.log_to_file("INFO","NoSuchElementException in TransactionTrackerOperations.get_CM_parcels()")
                    next_button = self.driver.find_element_by_xpath(LocalElementLocator.NEXT_SEARCH_BTN)

                    if (next_button.is_enabled()):
                        next_button = self.driver.find_element_by_xpath(LocalElementLocator.NEXT_SEARCH_BTN)
                        next_button.click()
                        time.sleep(2)

                    else:
                        print(without_error_parcel_count)
                        print("=======================================================================================")
                        print(without_error_parcel_comment)
                        print("=======================================================================================")
                        print(error_parcel_comment)
                        print("=======================================================================================")
                        excel_operations_object.set_value(row, 6, without_error_parcel_count)
                        excel_operations_object.set_value(row, 7, without_error_parcel_comment)
                        excel_operations_object.set_value(row, 8, error_parcel_comment)
                        self.driver.get(LocalElementLocator.TRANSACTION_TRACKER_PROD_LINK)
                        break
            except NoSuchElementException:
                break
        try:
            parcel_id1 = self.driver.find_element_by_xpath(LocalElementLocator.LAST_PARCEL_ID).text
        except NoSuchElementException:
            self.driver.get(LocalElementLocator.TRANSACTION_TRACKER_PROD_LINK)
            whilevalue==0
            time.sleep(2)



    # method for collect all unique parcels and fill input sheet as per result data
    def get_all_parcels(self, input_sheet, row):
        self.log.log_to_file("INFO", "Executing TransactionTrackerOperations.get_all_parcels()")
        time.sleep(2)
        whilevalue = 1
        while (whilevalue):
            try:
                selenium_operations_object = SeleniumOperations(self.v_task_type, self.driver, self.log)
                excel_operations_object = ExcelOperations(self.v_task_type, input_sheet)
                error_parcel_comment = ''
                without_error_parcel_comment = ''
                without_error_parcel_count = 0
                error_parcel_count = 0
                v_start = 1
                while (1):
                    v_second_start = 1
                    parcel_id = self.driver.find_element_by_xpath(LocalElementLocator.PARCEL_ID_1 + str(v_second_start) + LocalElementLocator.PARCEL_ID_2)
                    while (parcel_id.is_enabled()):
                        try:
                            parcel_id1 = self.driver.find_element_by_xpath(LocalElementLocator.PARCEL_ID_1 + str(v_second_start) + LocalElementLocator.PARCEL_ID_2).text
                        except NoSuchElementException:
                            break

                        v_status= selenium_operations_object.get_text_by_xpath(LocalElementLocator.STATUS_1 + str(v_second_start) + LocalElementLocator.STATUS_2)
                        v_document_id=selenium_operations_object.get_text_by_xpath(LocalElementLocator.DOCUMENT_ID_1 + str(v_second_start) + LocalElementLocator.DOCUMENT_ID_2)
                        v_parcel_date_time = selenium_operations_object.get_text_by_xpath(LocalElementLocator.PARCEL_DATE_TIME_1 + str(v_second_start) + LocalElementLocator.PARCEL_DATE_TIME_2)
                        if "Completed w/o Errors" in v_status:
                            without_error_parcel_count = without_error_parcel_count + 1
                            without_error_parcel_comment = without_error_parcel_comment + str(
                                without_error_parcel_count) + ") Parcel ID: " + str(
                                parcel_id1) + " (Document ID: " + str(
                                v_document_id) + ") with status: " + str(v_status) + " [" + v_parcel_date_time + "]" + "\n"
                        if "Completed w/Errors" in v_status:
                            error_parcel_count = error_parcel_count + 1
                            error_parcel_comment = error_parcel_comment + str(
                                error_parcel_count) + ") Parcel ID: " + str(
                                parcel_id1) + " (Document ID: " + str(v_document_id) + ") with status: " + str(
                                v_status) + " [" + v_parcel_date_time + "]" + "\n"
                        v_second_start = v_second_start + 1
                        v_start = v_start + 1
                        try:
                            parcel_id = self.driver.find_element_by_xpath(LocalElementLocator.PARCEL_ID_1 + str(v_second_start) + LocalElementLocator.PARCEL_ID_2)
                        except NoSuchElementException:
                            self.log.log_to_file("INFO",
                                                "NoSuchElementException in TransactionTrackerOperations.get_all_parcels()")

                    next_button = self.driver.find_element_by_xpath(LocalElementLocator.NEXT_SEARCH_BTN)

                    if (next_button.is_enabled()):
                        next_button = self.driver.find_element_by_xpath(LocalElementLocator.NEXT_SEARCH_BTN)
                        next_button.click()
                        time.sleep(2)

                    else:
                        excel_operations_object.set_value(row, 6, without_error_parcel_count)
                        excel_operations_object.set_value(row, 7, without_error_parcel_comment)
                        excel_operations_object.set_value(row, 8, error_parcel_comment)
                        self.driver.get(LocalElementLocator.TRANSACTION_TRACKER_PROD_LINK)
                        break
            except NoSuchElementException:
                break
        try:
            parcel_id1 = self.driver.find_element_by_xpath(LocalElementLocator.LAST_PARCEL_ID).text
        except NoSuchElementException:
            self.driver.get(LocalElementLocator.TRANSACTION_TRACKER_PROD_LINK)
            whilevalue==0
            time.sleep(2)


    # method for searching Credit Memo data with supplier,retailer,doc_type,date,input_sheet,row parameters
    def search_process_for_CMPDM(self,supplier,retailer,doc_type,date, input_sheet,row):
        print("Task no: "+str(row))
        print("--------------")
        try:
            self.log.log_to_file("INFO", "Executing TransactionTrackerOperations.search_process_for_CMPDM() for: "+str(supplier)+"|"+str(retailer)+"|"+str(doc_type))
            self.driver.switch_to.frame(0)
            selenium_operations_object = SeleniumOperations(self.v_task_type, self.driver, self.log)
            self.select_customer("Company",supplier)
            self.select_customer("Trading Partner",retailer)
            selenium_operations_object.send_text_by_xpath(LocalElementLocator.START_DATE,date)
            selenium_operations_object.click_element_by_xpath(LocalElementLocator.SERVICE)
            selenium_operations_object.click_element_by_xpath(LocalElementLocator.DC4ROUTER)
            selenium_operations_object.send_text_by_xpath(LocalElementLocator.DOCUMENT_TYPE,doc_type)
            selenium_operations_object.click_element_by_xpath(LocalElementLocator.SEARCH_BTN)
            time.sleep(3)
            self.get_CM_parcels(input_sheet, row)
        except NoSuchElementException:
            self.log.log_to_file("ERROR",
                                "Fail in TransactionTrackerOperations.search_process_for_CMPDM() for: " + str(
                                    supplier) + "|" + str(retailer) + "|" + str(doc_type))



    # method for searching all unique data with supplier,retailer,doc_type,date,input_sheet,row parameters
    def search_process_for_PDM(self,supplier,retailer,doc_type,date, input_sheet,row):
        print("Task NO : "+str(row) )
        print("----------------")
        try:
            self.log.log_to_file("INFO",
                                "Executing TransactionTrackerOperations.search_process_for_PDM() for: " + str(
                                    supplier) + "|" + str(retailer) + "|" + str(doc_type))
            self.driver.switch_to.frame(0)
            selenium_operations_object = SeleniumOperations(self.v_task_type, self.driver, self.log)
            self.select_customer("Company", supplier)
            self.select_customer("Trading Partner", retailer)
            selenium_operations_object.send_text_by_xpath(LocalElementLocator.START_DATE, date)
            selenium_operations_object.click_element_by_xpath(LocalElementLocator.SERVICE)
            selenium_operations_object.click_element_by_xpath(LocalElementLocator.DC4ROUTER)
            selenium_operations_object.send_text_by_xpath(LocalElementLocator.DOCUMENT_TYPE, doc_type)
            selenium_operations_object.click_element_by_xpath(LocalElementLocator.SEARCH_BTN)
            time.sleep(3)
            self.get_all_parcels(input_sheet, row)
            time.sleep(2)
        except NoSuchElementException:
            self.log.log_to_file("ERROR",
                                "Fail in TransactionTrackerOperations.search_process_for_PDM() for: " + str(
                                    supplier) + "|" + str(retailer) + "|" + str(doc_type))


    #method to sort "InProgress" tasks and "Monitoring Done" tasks
    def TaskFilter_for_CM_PDM(self,v_input_wb, status):
        self.log.log_to_file("INFO", "Executing CMProductionDataMonitoring.TaskFilter()")
        report_file_utility_object = ReportFileUtility(self.v_task_type)
        row_count = self.v_input_sheet.max_row
        if status == 'InProgress':
            self.log.log_to_file("INFO", "select InProgress task from input sheet from CMProductionDataMonitoring.TaskFilter()")
            excel_operations_object = ExcelOperations(self.v_task_type, self.v_input_sheet)
            for count in range(1, row_count + 1):
                v_start_time = time.time()
                if ((self.v_input_sheet.cell(row=count, column=5).value) == "InProgress"):
                    try:
                        v_supplier_name = self.v_input_sheet.cell(row=count, column=1).value
                        v_retailer_name = self.v_input_sheet.cell(row=count, column=2).value
                        v_doc_type=self.v_input_sheet.cell(row=count, column=3).value
                        v_date=self.v_input_sheet.cell(row=count, column=4).value
                        self.search_process_for_CMPDM(v_supplier_name,v_retailer_name,v_doc_type,v_date, self.v_input_sheet,count)
                        self.v_input_wb.save(AppConstants.INPUT_FILE_PATH)
                        v_end_time = time.time()
                        report_file_utility_object.update_sheet(self.v_username, 1, math.floor(v_end_time - v_start_time),str(datetime.date.today()),"PASS")
                        self.v_driver.refresh()
                        time.sleep(2)
                        v_found_parcels= self.v_input_sheet.cell(row=count, column=6).value

                        #logic for change status of task
                        if int(v_found_parcels)>=3:
                            excel_operations_object.set_value(count,5,"Monitoring done")
                        self.v_input_wb.save(AppConstants.INPUT_FILE_PATH)
                    except Exception:
                        self.log.log_to_file("ERROR", "Error in CMProductionDataMonitoring.TaskFilter()")
                        v_end_time = time.time()
                        report_file_utility_object.update_sheet(self.v_username, 1, math.floor(v_end_time - v_start_time),str(datetime.date.today()),"FAIL")
                        self.v_driver.refresh()
                        time.sleep(4)



   # method to sort "InProgress" tasks and "Monitoring Done" tasks
    def TaskFilter_for_PDM(self, status):
        self.log.log_to_file("INFO", "Executing ProductionDataMonitoring.TaskFilter()")
        report_file_utility_object = ReportFileUtility(self.v_task_type)
        v_row_count = self.v_input_sheet.max_row
        if status == 'InProgress':
            self.log.log_to_file("INFO",
                                "Select InProgress task from input sheet from ProductionDataMonitoring.TaskFilter()")
            excel_operations_object = ExcelOperations(self.v_task_type, self.v_input_sheet)
            for count in range(1, v_row_count + 1):
                v_start_time = time.time()
                if ((self.v_input_sheet.cell(row=count, column=5).value) == "InProgress"):
                    try:
                        v_supplier_name = self.v_input_sheet.cell(row=count, column=1).value
                        v_retailer_name = self.v_input_sheet.cell(row=count, column=2).value
                        v_doc_type=self.v_input_sheet.cell(row=count, column=3).value
                        v_date=self.v_input_sheet.cell(row=count, column=4).value
                        self.search_process_for_PDM(v_supplier_name,v_retailer_name,v_doc_type,v_date, self.v_input_sheet,count)
                        self.v_input_wb.save(AppConstants.INPUT_FILE_PATH)
                        v_end_time = time.time()
                        report_file_utility_object.update_sheet(self.v_username, 1, math.floor(v_end_time - v_start_time),str(datetime.date.today()),"PASS")
                        v_found_parcels= self.v_input_sheet.cell(row=count, column=6).value

                        #logic for change status of task
                        if int(v_found_parcels)>=4:
                            excel_operations_object.set_value(count,5,"Monitoring done")
                        self.v_input_wb.save(AppConstants.INPUT_FILE_PATH)
                    except Exception:
                        self.log.log_to_file("ERROR", "Error in ProductionDataMonitoring.TaskFilter()")
                        v_end_time = time.time()
                        report_file_utility_object.update_sheet(self.v_username, 1, math.floor(v_end_time - v_start_time),
                                        str(datetime.date.today()), "FAIL")
                        self.v_driver.refresh()
                        time.sleep(4)
