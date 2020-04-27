'''
@ Author - Aditya Datar
@ Creation date - 24/09/2018
@ Description - Declares all the constants to be used at the Process Level.
'''

TRANSACTION_TRACKER_PROD_LINK='https://commerce.spscommerce.com/transaction-tracker/prod/transactions/'
# XPath for Supplier Link
Supplier_Link = '//*[@id="table1:10:commandLink2"]'


# Common Locators of Customer View Page

Relationship_Tab = '//*[@id="form1:panelPage1"]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr/td[3]/a'
Profile_tab = '//*[@id="form1:panelPage1"]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr/td[5]/a'

# Trading Partner search XPath for relationship

Trading_Partner_Name = '//*[@id="form1:inputText1"]'
click_search = '//*[@id="form1:commandButton1"]'
Trading_Partner_Profile_Name = '//*[@id="form1:table1:0:outputText3"]'
Supplier_EDI_Info = '//*[@id="form1:table1"]/table[2]/tbody/tr[2]/td[5]'
Retailer_EDI_Info = '//*[@id="form1:table1"]/table[2]/tbody/tr[2]/td[7]'
Supplier_Profile_Link= '//*[@id="form1:table1:0:commandLink3"]'

# Profile Page XPaths
show_click = '//*[@id="form1:table1"]/table[2]/tbody/tr[2]/td[2]/div/a[2]'
Service_Name = 'FItoService'
Document_Type = '850'
