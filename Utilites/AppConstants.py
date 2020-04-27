'''
@ Author - Shilpa Chatterjee Roy
@ Creation date - 07/06/2018
@ Description - Declares all the constants to be used at the framework level.
'''

#Common Constants
BROWSER_DRIVER = "../BrowserDrivers/chromedriver.exe"
LOG_FILE_BASE_PATH = "../Logs"
REPORT_FILE_BASE_PATH = "../Reports"
RUNNER_ENVIRONMENT = "../X-Runner/RunnerEnv.xlsx"
LOGIN_ENVIRONMENT_LOCATOR_FILE_PATH = "../Resources/Login_Locators_Environment_File.xlsx"

INPUT_FILE_PATH = "../X-Runner/Input.xlsx"
CLIENT_SECRET_JSON_FILE_PATH = '../Resources/client_secret.json'


#Workflow wise Constants
#------------------------------------------------------------------------------------------

#Team and track list

TRACK_LIST = ['QB Setup']
TEAM_LIST = ['QB']


# TRACK_LIST = ['Production Data Monitoring','Credit Memo Production Data Monitoring', 'Error Hospital', 'Netsuite Review 850','Process Test Files','RPA']
# TEAM_LIST = ['WAIT', 'DNI', 'NETSUITE', '3PL', 'ICE', 'PREMIER', 'TRANSACTION TRIAGE', 'BCM', 'QUICK BOOKS',
#                       'UN PARTNER', 'SPS','Service Time card']

#Usefull Links
DC4_PROD_LINK = "http://dc4ui.p01.pro:7777/dc4custmanager/faces/home.jsp"
DC4_PREPROD_LINK = "http://dc4ui.p01.ppd:7777/dc4custmanager/faces/home.jsp"
JIRA_LINK = "https://atlassian.spscommerce.com/login.jsp"
LAUNCHPAD_LINK = "https://commerce.spscommerce.com/auth/login/"
I_AM_TOOL_LINK = "https://iam.spscommerce.com/login/login"
SALESFORCE_LINK = "https://spscommerce.my.salesforce.com/?ec=302&startURL=%2Fhome%2Fhome.jsp"


#Common Xpaths
#DC4 UI
DC4_TAB = 'form1:commandLink1'
DC4_COMPANY_NAME_TEXT_FIELD = '//*[@id="inputText41"]'
DC4_COMPANY_NAME_SEARCH_CLICK = '//*[@id="commandButton12"]'
DC4_COMPANY_SEARCH_BY_EDI_INFO_TAB = 'showDetailItem2'
DC4_COMPANY_SEARCH_BY_ISA_ID_TEXT_FIELD = 'inputText49'
DC4_COMPANY_SEARCH_BY_ISA_ID_SEARCH_TAB = 'commandButton14'

DC4_COMPANY_SEARCH_BY_TPID_TAB = 'showDetailItem3'
DC4_COMPANY_SEARCH_BY_TPID_TEXT_FIELD = 'inputText66'
DC4_COMPANY_SEARCH_BY_TPID_SEARCH_TAB = 'commandButton16'


#Salsesforce
SAILPOINT_TAB = '//*[@id="idp_section_buttons"]/button'
SALESFORCE_TAB = '//*[@id="slpt-launchpad-launcher-salesforce-btnInnerEl"]'

#FTP paths

FTP_PRE_PROD_LINK=""
#TransactionTrackerXpaths
