'''

@ Author - Karan Pandya
@ Creation date - 08/29/2018
@ Description - Main Script of Production Data Monitoring
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

class NetsuiteReview850:
    def __init__(self, task_type, lo, username):
        self.v_task_type = task_type
        self.v_driver = webdriver.Chrome(AppConstants.BROWSER_DRIVER)
        self.v_input_wb = openpyxl.load_workbook(AppConstants.INPUT_FILE_PATH)
        self.lo = lo
        self.v_username = username

    def execute_main(self):
        v_start_time = time.time()
        self.lo.log_to_file("INFO", "Login in to DC4 Prod")
        lg = Login(self.v_task_type, self.v_driver, self.v_input_wb, self.lo)
        so = SeleniumOperations(self.v_task_type,self.v_driver,self.lo)
        rf = ReportFileUtility(self.v_task_type)

        lg.login("DC4 Prod")

        #so.click_element(AppConstants.DC4_TAB, "BY_NAME")
        dc = DC4_Utility(self.v_task_type, self.v_driver, self.lo)
        dc.company_search_by_name('Midlab Inc')
        #dc.company_search_by_ISA_ID('6166651648')
        #dc.company_search_by_TPID('620TSTWONDERTRE')

        self.v_driver.close()
        v_end_time = time.time()
        rf.update_sheet(self.v_username, 2, math.floor(v_end_time - v_start_time), str(datetime.date.today()))





