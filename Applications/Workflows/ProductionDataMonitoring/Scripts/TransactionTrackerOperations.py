'''

@ Author - Yogesh Pawar
@ Creation date - 09/21/2018
@ Description - Common Transaction Tracker Operation
'''

from Utilites import AppConstants
from Utilites.SeleniumOperations import SeleniumOperations
from Utilites.LogFileUtility import LogFileUtility
from Utilites.ExcelOperations import ExcelOperations
from Applications.Workflows.ProductionDataMonitoring.AppResources import LocalElementLocator
import time
import openpyxl

class TransactionTrackerOperations:
    def __init__(self, task_type, driver, lo):
        self.v_input_wb = openpyxl.load_workbook(AppConstants.INPUT_FILE_PATH)
        self.v_task_type = task_type
        self.v_input_sheet = self.v_input_wb.get_sheet_by_name("CreditMemoInputData")
        self.driver = driver
        self.lo = lo

    # Methode for select supplier and retailer wth two parameter i.e supplier name and retailer name
    def select_customer(self, customer_type, customer_name):

        self.lo.log_to_file("INFO", "Executing method 'select_customer' from TransactionTrackerOperations")
        so = SeleniumOperations(self.v_task_type, self.driver, self.lo)
        print("Search for: " + str(customer_name))

        time.sleep(2)
        #driver.switch_to.frame(0)
        if customer_type == "Company":
            #self.driver.switch_to.frame(0)

            self.driver.find_element_by_xpath(
                "html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/label/chosen-company/div/ul/li/input").send_keys(
                customer_name)
        if customer_type == "Trading Partner":
            #self.driver.switch_to.frame(0)
            TP_name = self.driver.find_element_by_xpath(
                "html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/div[4]/label/chosen-trading-partner/div/ul/li/input")
            time.sleep(2)
            # driver.find_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/div[4]/label/chosen-trading-partner/div/ul").click()
            TP_name.send_keys(customer_name)

        time.sleep(2)
        count = self.driver.find_elements_by_xpath(".//*[contains(@id,'ui-select-choices-row-')]")
        for i in range(len(count)):
            if customer_type == "Company":
                customer_from_TT = self.driver.find_element_by_xpath(
                    ".//*[@id='ui-select-choices-row-0-" + str(i) + "']").text
            if customer_type == "Trading Partner":
                customer_from_TT = self.driver.find_element_by_xpath(
                    ".//*[@id='ui-select-choices-row-1-" + str(i) + "']").text
            if customer_name.lower() == customer_from_TT.lower():
                if customer_type == "Company":
                    self.driver.find_element_by_xpath(".//*[@id='ui-select-choices-row-0-" + str(i) + "']").click()
                if customer_type == "Trading Partner":
                    self.driver.find_element_by_xpath(".//*[@id='ui-select-choices-row-1-" + str(i) + "']").click()
                print("Found matching customer name at position: " + str(i + 1))
        time.sleep(2)

    #search Data type
    def search_datatype(self):
        self.lo.log_to_file("INFO", "Executing method 'search_datatype' from TransactionTrackerOperations")
        so = SeleniumOperations(self.v_task_type, self.driver, self.lo)


    # Methode for get parcels detailes and update in inpute sheet from search reasult
    def get_parcel(self, input_sheet,row):
        self.lo.log_to_file("INFO", "Executing method 'get_parcel' from TransactionTrackerOperations")
        so = SeleniumOperations(self.v_task_type, self.driver, self.lo)
        eo = ExcelOperations(self.v_task_type, input_sheet)
        error_parcel_comment=''
        without_error_parcel_comment = ''
        #print("========================================================================================")
        parcel_count = int(self.driver.find_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/spsui-feedback-container[4]/result-feedback/div/div/div/div[1]/strong").text)
        print("Total unique parcel count is: "+str(parcel_count))
        without_error_parcel_count=0
        error_parcel_count=0
        for i in range (parcel_count):
            document_id=self.driver.find_element_by_xpath(".//*[@id='parentTablesContainer']/div[2]/table/tbody[1]/tr["+str(i+1)+"]/td[5]").text
            status=self.driver.find_element_by_xpath(".//*[@id='parentTablesContainer']/div[2]/table/tbody[1]/tr["+str(i+1)+"]/td[1]").text
            parcel_ID=self.driver.find_element_by_xpath(".//*[@id='parentTablesContainer']/div[1]/table/tbody/tr["+str(i+1)+"]/td[2]/span/a").text

            print(str(i+1)+") Parcel ID: "+str(parcel_ID)+" (Document ID: "+str(document_id)+") with status: "+str(status))

            if "Completed w/o Errors" in status:
                without_error_parcel_count = without_error_parcel_count + 1
                without_error_parcel_comment=without_error_parcel_comment+str(without_error_parcel_count)+") Parcel ID: "+str(parcel_ID)+" (Document ID: "+str(document_id)+") with status: "+str(status)+"\n"


            if "Completed w/Errors" in status:
                error_parcel_count=error_parcel_count+1
                error_parcel_comment=error_parcel_comment+str(error_parcel_count)+") Parcel ID: "+str(parcel_ID)+" (Document ID: "+str(document_id)+") with status: "+str(status)
                #eo.set_value(row, 8, "Data found for CREDIT MEMO")

                #comment=comment+"Credir Memo not found in Search result"+"\n"
                #comment = comment + str(i + 1) + ") Parcel ID: " + str(parcel_ID) + " (Document ID: " + str(document_id) + ") with status: " + str(status)

        #print("========================================================================================")
        eo.set_value(row,6,without_error_parcel_count)
        eo.set_value(row, 7, without_error_parcel_comment)
        eo.set_value(row, 8, error_parcel_comment)
        self.driver.get("https://commerce.spscommerce.com/transaction-tracker/prod/transactions/")
        #so.click_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[5]/div/a")
        time.sleep(5)


    def get_credit_memo_parcel(self, input_sheet,row):
        self.lo.log_to_file("INFO", "Executing method 'get_parcel' from TransactionTrackerOperations")
        so = SeleniumOperations(self.v_task_type, self.driver, self.lo)
        eo = ExcelOperations(self.v_task_type, input_sheet)
        error_parcel_comment = ''
        without_error_parcel_comment = ''
        #comment = ''
        cm_comment=''
        #print("========================================================================================")
        parcel_count=int(so.get_text_by_xpath("html/body/div[1]/section/section/div/div/section/div/spsui-feedback-container[4]/result-feedback/div/div/div/div[1]/strong"))
        #parcel_count = int(self.driver.find_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/spsui-feedback-container[4]/result-feedback/div/div/div/div[1]/strong").text)
        print("Total unique parcel count is: "+str(parcel_count))
        cm_parcel_count=0
        without_error_parcel_count = 0
        error_parcel_count = 0
        for i in range (parcel_count):
            document_id=self.driver.find_element_by_xpath(".//*[@id='parentTablesContainer']/div[2]/table/tbody[1]/tr["+str(i+1)+"]/td[5]").text
            status=self.driver.find_element_by_xpath(".//*[@id='parentTablesContainer']/div[2]/table/tbody[1]/tr["+str(i+1)+"]/td[1]").text
            parcel_ID=self.driver.find_element_by_xpath(".//*[@id='parentTablesContainer']/div[1]/table/tbody/tr["+str(i+1)+"]/td[2]/span/a").text

            #print(str(i+1)+") Parcel ID: "+str(parcel_ID)+" (Document ID: "+str(document_id)+") with status: "+str(status))
            #comment=comment+str(i+1)+") Parcel ID: "+str(parcel_ID)+" (Document ID: "+str(document_id)+") with status: "+str(status)+"\n"
            if "CM" in document_id:
                # cm_comment = cm_comment + str(cm_parcel_count + 1) + ") Parcel ID: " + str(parcel_ID) + " (Document ID: " + str(
                #     document_id) + ") with status: " + str(status) + "\n"
                # cm_parcel_count=cm_parcel_count+1
                # print(str(cm_parcel_count + 1) + ") Parcel ID: " + str(parcel_ID) + " (Document ID: " + str(
                #     document_id) + ") with status: " + str(status))

                if "Completed w/o Errors" in status:
                    without_error_parcel_count = without_error_parcel_count + 1
                    without_error_parcel_comment = without_error_parcel_comment + str(
                        without_error_parcel_count) + ") Parcel ID: " + str(parcel_ID) + " (Document ID: " + str(
                        document_id) + ") with status: " + str(status) + "\n"
                    print(without_error_parcel_comment)

                if "Completed w/Errors" in status:
                    error_parcel_count = error_parcel_count + 1
                    error_parcel_comment = error_parcel_comment + str(error_parcel_count) + ") Parcel ID: " + str(
                        parcel_ID) + " (Document ID: " + str(document_id) + ") with status: " + str(status)
                    print(error_parcel_comment)

                #eo.set_value(row, 8, "Data found for CREDIT MEMO")

                #comment=comment+"Credir Memo not found in Search result"+"\n"
                #comment = comment + str(i + 1) + ") Parcel ID: " + str(parcel_ID) + " (Document ID: " + str(document_id) + ") with status: " + str(status)

        #print("========================================================================================")

        eo.set_value(row, 6, without_error_parcel_count)
        eo.set_value(row, 7, without_error_parcel_comment)
        eo.set_value(row, 8, error_parcel_comment)

        self.driver.get("https://commerce.spscommerce.com/transaction-tracker/prod/transactions/")
        #so.click_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[5]/div/a")
        time.sleep(5)
        return cm_comment


    # Methode for execute search process for Premier Normal PDM task
    def search_process_for_PDM(self,supplier,retailer,doc_type,date, input_sheet,row):

        print("=====================================Task Number: "+str(row)+"===================================")
        print("============================================================================================")
        self.lo.log_to_file("INFO", "Executing method 'search_process' from TransactionTrackerOperations")
        self.driver.switch_to.frame(0)
        so = SeleniumOperations(self.v_task_type, self.driver, self.lo)
        self.select_customer("Company",supplier)
        self.select_customer("Trading Partner",retailer)

        start_date = self.driver.find_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/label/input")
        time.sleep(2)
        start_date.clear()
        start_date.send_keys(date)
        time.sleep(2)
        service=self.driver.find_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/label/select")
        service.send_keys("DC4Router")
        time.sleep(2)
        document_type=self.driver.find_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div[3]/label/input")
        document_type.send_keys(doc_type)
        time.sleep(2)
        search_btn = self.driver.find_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[5]/div/button")
        search_btn.click()
        time.sleep(3)
        clear_btn = self.driver.find_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[5]/div/a")
        #clear_btn.click()
        if str(row)==str(2):
            time.sleep(1)
            self.driver.find_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[3]/div[1]/ul/li[2]/label/select").send_keys("100")
            #so.send_text_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[3]/div[1]/ul/li[2]/label/select","100")
            time.sleep(2)
        #self.get_parcel(input_sheet,row)
        self.get_parcel(input_sheet, row)



    # Methode for execute search process for Premier Credit Memo PDM task
    def search_process_for_CMPDM(self,supplier,retailer,doc_type,date, input_sheet,row):

        print("=====================================Task Number: "+str(row)+"===================================")
        print("============================================================================================")
        self.lo.log_to_file("INFO", "Executing method 'search_process' from TransactionTrackerOperations")
        self.driver.switch_to.frame(0)
        so = SeleniumOperations(self.v_task_type, self.driver, self.lo)
        self.select_customer("Company",supplier)
        self.select_customer("Trading Partner",retailer)

        start_date = self.driver.find_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/label/input")
        time.sleep(2)
        start_date.clear()
        start_date.send_keys(date)
        time.sleep(2)
        service=self.driver.find_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/label/select")
        service.send_keys("DC4Router")
        time.sleep(2)
        document_type=self.driver.find_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div[3]/label/input")
        document_type.send_keys(doc_type)
        time.sleep(2)
        search_btn = self.driver.find_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[5]/div/button")
        search_btn.click()
        time.sleep(3)

        #logic for show all 100 parcels
        if str(row)==str(2):
            time.sleep(1)
            self.driver.find_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[3]/div[1]/ul/li[2]/label/select").send_keys("100")
            #so.send_text_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[3]/div[1]/ul/li[2]/label/select","100")
            time.sleep(2)

        # current_parcels = so.get_text_by_xpath("html/body/div[1]/section/section/div/div/section/div/spsui-feedback-container[4]/result-feedback/div/div/div/div[1]/strong")
        #
        # total_parcels=so.get_text_by_xpath("html/body/div[1]/section/section/div/div/section/div/spsui-feedback-container[4]/result-feedback/div/div/div/div[1]/strong")
        #
        # def total_tt_pages(total_parcels):
        #     a = divmod(total_parcels, 100)
        #     if a[1] > 0:
        #         return int(a[0] + 1)
        #     else:
        #         return int(a[0])
        #
        # eo = ExcelOperations(self.v_task_type, self.v_input_sheet)
        # pages=total_tt_pages(int(total_parcels))
        #
        # if pages==1:
        #     self.get_credit_memo_parcel(input_sheet, row)
        # else:
        #     cm_comment = ''
        #     for i in int(pages):
        #         cm_comment=cm_comment+self.get_credit_memo_parcel(input_sheet, row)
        #
        #
        #         if i != pages - 1:
        #             so.click_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[3]/div[3]/ul/li[5]/p/span/button[2]")
        #     eo.set_value(row, 7, cm_comment)
        #     self.v_input_wb.save(AppConstants.INPUT_FILE_PATH)
        #
        #
        # if int(current_parcels)==int(total_parcels):
        #     print(str(current_parcels)+"====Equals======="+str(total_parcels))
        #     self.get_credit_memo_parcel(input_sheet, row)
        #
        # else:
        #     print(str(current_parcels) + "=====else======" + str(total_parcels))
        #
        # # print("current page: " + str(current_page))
        # # print("Total pages: "+str(page_out_of))

        self.get_credit_memo_parcel(input_sheet, row)

    # Methode for execute search process for process for Process Test File task
    def search_process_for_final_850(self,supplier,retailer,doc_type,date, input_sheet,row):

        print("=====================================Task Number: "+str(row)+"===================================")
        print("============================================================================================")
        self.lo.log_to_file("INFO", "Executing method 'search_process' from TransactionTrackerOperations")
        self.driver.switch_to.frame(0)
        so = SeleniumOperations(self.v_task_type, self.driver, self.lo)
        self.select_customer("Company",supplier)
        self.select_customer("Trading Partner",retailer)

        start_date = self.driver.find_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/label/input")
        #time.sleep(2)
        start_date.clear()
        start_date.send_keys(date)
        #time.sleep(2)
        service=self.driver.find_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/label/select")
        service.send_keys("DC4Router")
        time.sleep(2)
        document_type=self.driver.find_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div[3]/label/input")
        document_type.send_keys(doc_type)
        time.sleep(2)
        search_btn = self.driver.find_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[5]/div/button")
        search_btn.click()
        time.sleep(3)
        clear_btn = self.driver.find_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[5]/div/a")
        #clear_btn.click()
        #self.get_parcel(input_sheet,row)

    # Methode for execute search process for process for Process Test File task
    def search_process_for_process_test_file(self, supplier, retailer, doc_type,date, input_sheet,row):

        print("=====================================Task Number: " + str(row-1) + "===================================")
        print("============================================================================================")
        self.lo.log_to_file("INFO", "Executing method 'search_process_for_process_test_file' from TransactionTrackerOperations")
        self.driver.switch_to.frame(0)
        so = SeleniumOperations(self.v_task_type, self.driver, self.lo)
        self.select_customer("Company", supplier)
        self.select_customer("Trading Partner", retailer)

        start_date = self.driver.find_element_by_xpath(
            "html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/label/input")
        time.sleep(2)
        start_date.clear()
        start_date.send_keys(date)
        time.sleep(2)
        service = self.driver.find_element_by_xpath(
            "html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/label/select")
        service.send_keys("DC4Router")
        time.sleep(2)
        document_type = self.driver.find_element_by_xpath(
            "html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div[3]/label/input")
        document_type.send_keys(doc_type)
        time.sleep(2)
        search_btn = self.driver.find_element_by_xpath(
            "html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[5]/div/button")
        search_btn.click()
        time.sleep(3)
        clear_btn = self.driver.find_element_by_xpath(
            "html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[5]/div/a")
        # clear_btn.click()
        #self.get_parcel(input_sheet, row)

    # Method to open Transaction Tracker and search by Parcel ID
    def search_parcel_id(self, parcel_id):
        self.driver.get("https://commerce.spscommerce.com/transaction-tracker/prod/transactions/")
        time.sleep(4)
        self.driver.switch_to.frame(0)
        parcel_id_textbox = self.driver.find_element_by_xpath(
            "html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/label/div/div[2]/input")
        parcel_id_textbox.send_keys(parcel_id)
        search_btn = self.driver.find_element_by_xpath(
            "html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[5]/div/button")
        search_btn.click()


    def download_first_parcel(self):
        so = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)
        time.sleep(4)

        first_parcel_id = self.driver.find_element_by_xpath(
            ".//*[@id='parentTablesContainer']/div[1]/table/tbody/tr/td[2]/span/a")

        first_parcel_id.click()
        time.sleep(2)
        file = open("D://TTcode.txt", "w+")
        file.write(self.driver.page_source)
        print(file.read())
        # btn=self.driver.find_element_by_xpath("//div[@ng-repeat='parcel in vm.transaction.parcels'][1]//a/i[@class='fa fa-file document-icon brandblue']")
        # btn.click()
