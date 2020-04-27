import openpyxl
from Applications.Workflows.ServiceTimeCard.TaskCategorization.AppResources import ElementLocators
from selenium import webdriver
from Utilites.SeleniumOperations import SeleniumOperations
from Applications.Workflows.ServiceTimeCard.TaskCategorization.Script.Salesforce import Salesforce
import time

class Task_Categorization_Main_Test_Script:

    def __init__(self, task_type, lo, username):


        self.v_input_wb = openpyxl.load_workbook(ElementLocators.INPUT_FILE_PATH)
        self.v_task_type = task_type
        self.v_input_sheet = self.v_input_wb.get_sheet_by_name("Input")
        self.log = lo
        self.v_username = username
        self.v_Browser = webdriver.Chrome(ElementLocators.BROWSER_DRIVER)
        self.v_Browser.maximize_window()
        self.sf=Salesforce(task_type, lo, username,self.v_Browser)

    def execute_main(self):


        self.sf.login_to_sailpoint()
        self.sf.open_FS_Team_Queue()
        Case_number_and_salesforce_id_array=self.sf.get_all_ticket_info()
        self.sf.open_cases_and_get_info(Case_number_and_salesforce_id_array)



        time.sleep(585)