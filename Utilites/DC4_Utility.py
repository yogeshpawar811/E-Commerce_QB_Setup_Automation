'''

@ Author - Karan Pandya
@ Creation date - 08/31/2018
@ Description - Common DC4 Prod Operation
'''
from Utilites import AppConstants
from Utilites.SeleniumOperations import SeleniumOperations
class DC4_Utility:
    def __init__(self, task_type, driver, lo):
        self.v_task_type = task_type
        self.v_driver = driver
        self.lo = lo


    def company_search_by_name(self, company_name):
        so = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)
        so.click_element_by_name(AppConstants.DC4_TAB)
        so.send_text_by_xpath(AppConstants.DC4_COMPANY_NAME_TEXT_FIELD, company_name)
        so.click_element_by_xpath(AppConstants.DC4_COMPANY_NAME_SEARCH_CLICK)

    def company_search_by_ISA_ID(self, ISA_ID):
        so = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)
        so.click_element_by_id(AppConstants.DC4_COMPANY_SEARCH_BY_EDI_INFO_TAB)
        so.send_text_by_id(AppConstants.DC4_COMPANY_SEARCH_BY_ISA_ID_TEXT_FIELD, ISA_ID)
        so.click_element_by_id(AppConstants.DC4_COMPANY_SEARCH_BY_ISA_ID_SEARCH_TAB)

    def company_search_by_TPID(self, TPID):
        so = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)
        so.click_element_by_id(AppConstants.DC4_COMPANY_SEARCH_BY_TPID_TAB)
        so.send_text_by_id(AppConstants.DC4_COMPANY_SEARCH_BY_TPID_TEXT_FIELD, TPID)
        so.click_element_by_id(AppConstants.DC4_COMPANY_SEARCH_BY_TPID_SEARCH_TAB)
