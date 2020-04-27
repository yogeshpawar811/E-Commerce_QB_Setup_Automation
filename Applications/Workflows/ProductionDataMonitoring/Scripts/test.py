'''

@ Author - Yogesh Pawar
@ Creation date - 10/07/2018
@ Description - Main Script of Credit Memo Production Data Monitoring
'''
import time
import math
import datetime
import openpyxl
from Utilites.Login import Login
from Utilites import AppConstants
from selenium import webdriver
from Utilites.LogFileUtility import LogFileUtility
from Utilites.DC4_Utility import DC4_Utility
from Utilites.SeleniumOperations import SeleniumOperations
from Utilites.ReportFileUtility import ReportFileUtility
from Applications.Workflows.ProductionDataMonitoring.AppResources import LocalElementLocator
from Applications.Workflows.ProductionDataMonitoring.Scripts.TransactionTrackerOperations2 import TransactionTrackerOperations
from Utilites.ExcelOperations import ExcelOperations


class CMProductionDataMonitoring:

    # def __init__(self, task_type, lo, username):
    #     self.v_input_wb = openpyxl.load_workbook(AppConstants.INPUT_FILE_PATH)
    #     self.v_task_type = task_type
    #     self.v_input_sheet = self.v_input_wb.get_sheet_by_name("CreditMemoInputData")
    #     self.lo = lo
    #     self.v_username = username
    #     print("in prod monitoring method")

    def execute_main(self):


        print('in main method of PDM')


        self.v_driver = webdriver.Chrome(AppConstants.BROWSER_DRIVER)
        self.v_driver.maximize_window()

        self.lo.log_to_file("INFO", "Login in to Launchpad")
        lg = Login(self.v_task_type, self.v_driver, self.v_input_wb, self.lo)
        so = SeleniumOperations(self.v_task_type,self.v_driver,self.lo)
        print("asdasdsad")
        lg.login("Launchpad")
        time.sleep(5)
        self.v_driver.get(LocalElementLocator.TRANSACTION_TRACKER_PROD_LINK)
        time.sleep(5)
        if so.check_clickable_by_xpath("html/body/app-reporting/div/div/nav-bar/div/nav"):
            print("Element clickable")
        else:
            print("Not clickable")
        # print("Browser opened,login,open TT")

