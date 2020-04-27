'''

@ Author - Karan Pandya
@ Creation date - 09/14/2018
@ Description - Error Hospital Operations
'''
from Utilites.SeleniumOperations import SeleniumOperations
from Applications.Workflows.ErrorHospital.AppResources import LocalElementLocator
import re
class ErrorHospital_Utility:
    def __init__(self, task_type, driver, lo):
        self.v_task_type = task_type
        self.v_driver = driver
        self.lo = lo

    def adhoc_error_search(self, Ticket_Uid, START_DATE, TPID):
        so = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)
        so.click_element_by_id(LocalElementLocator.ERROR_HOSPITAL_TAB_ID)
        so.send_text_by_id(LocalElementLocator.TICKET_UID_ID, Ticket_Uid)
        so.send_text_by_id(LocalElementLocator.TITLE_ID, LocalElementLocator.ADHOC_ERROR_TITLE)
        so.send_text_by_id(LocalElementLocator.DESCRIPTION_ID, '%No entry in the web trading partnership table%'+TPID+'%')
        so.send_text_by_id(LocalElementLocator.START_DATE_ID, START_DATE)
        so.click_element_by_id(LocalElementLocator.SEARCH_BUTTON_ID)

    def get_ticket_uid(self, index):
        so = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)
        #ticket_uid_path = '//*[@id="form1:table1:'+str(index)+':commandLink1"]'
        ticket_uid_path = '//*[@id="form1:table1"]/table[2]/tbody/tr['+str(index)+']/td[3]'

        if so.check_exists_by_xpath(ticket_uid_path):
            return so.get_text_by_xpath(ticket_uid_path)
        else:
            return False

    def get_sender_name(self, index):
        so = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)
        #sender_path = '//*[@id="form1:table1:' + str(index) + ':outputText15"]'
        sender_path = '//*[@id="form1:table1"]/table[2]/tbody/tr['+str(index)+']/td[6]'
        if so.check_exists_by_xpath(sender_path):
            return so.get_text_by_xpath(sender_path)
        else:
            return False

    def get_receiver_name(self, index):
        so = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)
        #receiver_path = '//*[@id="form1:table1:' + str(index) + ':outputText17"]'
        receiver_path = '//*[@id="form1:table1"]/table[2]/tbody/tr[' + str(index) + ']/td[7]'
        if so.check_exists_by_xpath(receiver_path):
            return so.get_text_by_xpath(receiver_path)
        else:
            return False


    def get_info_from_description(self, index):
        so = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)
        path = '//*[@id="form1:table1:'+str(index)+':commandLink1"]'
        so.click_element_by_xpath(path)
        doctype = so.get_text_by_xpath(LocalElementLocator.EH_DOCTYPE_INFO_XPATH)
        doctype = doctype.split(' ')[0]
        TPID = so.get_text_by_xpath(LocalElementLocator.EH_DESCRIPTION_INFO_XPATH)
        if 'Document:' in TPID:
            TPID = TPID.split('Document:')[1]
            TPID = TPID.split('\n')[0]
            #TPID = re.sub('\W+', '', TPID)

        else:
            TPID = 'Invalid TPID'
        return TPID, doctype

