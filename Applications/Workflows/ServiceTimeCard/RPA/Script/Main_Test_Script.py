'''
@ Author - Yogesh Pawar
@ Creation date - 01/10/2020
@ Description - Main Test Script of RPA
'''

import time
import openpyxl
from Utilites.Login import Login
from Utilites import AppConstants
from selenium import webdriver
from Applications.Workflows.ServiceTimeCard.RPA.AppResources import ElementLocators
from Applications.Workflows.ServiceTimeCard.RPA.Script.GrumpyTool_Actions import GrumpyTool_Actions
from Applications.Workflows.ProductionDataMonitoring.AppResources import LocalElementLocator
from Applications.Workflows.ProductionDataMonitoring.Scripts.ProductionDataMonitoring_TransactionTrackerOperations import TransactionTrackerOperations



class Main_Test_Script:

    def __init__(self, task_type, lo, username):


        self.v_input_wb = openpyxl.load_workbook(ElementLocators.INPUT_FILE_PATH)
        self.v_task_type = task_type
        self.v_input_sheet = self.v_input_wb.get_sheet_by_name("Input")
        self.log = lo
        self.v_username = username

        print("in init")

    # main method of CMProductionDataMonitoring
    def execute_main(self):
        print("Main_Test_Script")
        self.v_Browser = webdriver.Chrome(ElementLocators.BROWSER_DRIVER)
        self.v_Browser.maximize_window()
        self.v_Browser.get(GrumpyTool_Actions.customised_grumpy_url("06114772"))
        GrumpyTool_Actions.get_evision_docid(self.v_Browser)

        # self.v_Browser.find_element_by_xpath().te
        time.sleep(10)