'''
@ Author - Aditya Datar
@ Creation date - 24/09/2018
@ Description - Declares all the constants to be used at the Process Level.
'''

# XPath for Supplier Link
Company_Select_Link = '//*[@id="table1:10:commandLink2"]'

# Document type
PO_File = 850

# Common Locators of Customer View Page

Relationship_Tab = '//*[@id="form1:panelPage1"]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr/td[3]/a'
Profile_tab = '//*[@id="form1:panelPage1"]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr/td[5]/a'

# Trading Partner search XPath for relationship

Trading_Partner_Name_text_Field = '//*[@id="form1:inputText1"]'
Trading_Partner_Name = '//*[@id="form1:table1:0:commandLink2"]'
click_search = '//*[@id="form1:commandButton1"]'
Trading_Partner_Profile_Name = '//*[@id="form1:table1:0:outputText3"]'
Supplier_EDI_Info = '//*[@id="form1:table1"]/table[2]/tbody/tr[2]/td[5]'
Retailer_EDI_Info = '//*[@id="form1:table1"]/table[2]/tbody/tr[2]/td[7]'
Supplier_Profile_Link= '//*[@id="form1:table1:0:commandLink3"]'

# Profile Page XPaths
show_click = '//*[@id="form1:table1"]/table[2]/tbody/tr[2]/td[2]/div/a[2]'
Service_Name = 'FItoService'
Document_Type = '850'

# Setup Aggregator Link
Setup_Aggregator_Link = "https://commerce.spscommerce.com/setup-aggregator/aggregator/"

# XPaths of Setup Aggregator
Select_Environment = '/html/body/sa-root/div[2]/sa-aggregator-container/div/div[1]/sa-aggregator-preview/div/div[2]/div/div[1]/form/div[1]/p-dropdown/div/div[2]/span'
Select_Pre_Prod_Env = '/html/body/sa-root/div[2]/sa-aggregator-container/div/div[1]/sa-aggregator-preview/div/div[2]/div/div[1]/form/div[1]/p-dropdown/div/div[3]/div/ul/li[1]'
Retailer_Profile_Text_Field = '//input[@placeholder= "Search profile by name"]'

Select_Required_Profile = '/html/body/sa-root/div[2]/sa-aggregator-container/div/div[1]/sa-aggregator-preview/div/div[2]/div/div[1]/form/div[2]/div/p-autocomplete/span/div/ul/li'

#Download Parcels Paths

RUNNER_ENVIRONMENT = "../X-Runner/RunnerEnv.xlsx"

