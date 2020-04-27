'''

@ Author - Yogesh Pawar
@ Creation date - 08/29/2018
@ Description - Main Script of Production Data Monitoring
'''
import time
import openpyxl
from Utilites.Login import Login
from Utilites import AppConstants
from selenium import webdriver
from Applications.Workflows.ProductionDataMonitoring.AppResources import LocalElementLocator
from Applications.Workflows.ProductionDataMonitoring.Scripts.ProductionDataMonitoring_TransactionTrackerOperations import TransactionTrackerOperations


class ProductionDataMonitoring:

    def __init__(self, task_type, lo, username):
        self.v_input_wb = openpyxl.load_workbook(AppConstants.INPUT_FILE_PATH)
        self.v_task_type = task_type
        self.v_input_sheet = self.v_input_wb.get_sheet_by_name("InputData")
        self.log = lo
        self.v_username = username


    # main method of CMProductionDataMonitoring
    def execute_main(self):
        self.log.log_to_file("INFO", "Executing ProductionDataMonitoring.execute_main()")
        self.v_driver = webdriver.Chrome(AppConstants.BROWSER_DRIVER)
        self.v_driver.maximize_window()
        TransactionTrackerOperations_page_object = TransactionTrackerOperations(self.v_task_type, self.v_driver,self.log, self.v_input_sheet,self.v_input_wb, self.v_username,self.v_driver)
        login_operations_object = Login(self.v_task_type, self.v_driver, self.v_input_wb, self.log)
        login_operations_object.login("Launchpad")
        self.log.log_to_file("INFO", "Login in to Launchpad")
        time.sleep(5)
        self.v_driver.get(LocalElementLocator.TRANSACTION_TRACKER_PROD_LINK)
        TransactionTrackerOperations_page_object.TaskFilter_for_PDM(self.v_input_wb, 'InProgress')
        self.log.log_to_file("INFO", "completed ProductionDataMonitoring.execute_main()")
        self.v_driver.close()

