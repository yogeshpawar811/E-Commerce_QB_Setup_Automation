'''

@ Author - Karan Pandya
@ Creation date - 08/29/2018
@ Description - Selection of script as per user request
'''
from Utilites.LogFileUtility import LogFileUtility
from Applications.Workflows.ProductionDataMonitoring.Scripts.ProductionDataMonitoring import ProductionDataMonitoring
from Applications.Workflows.ProductionDataMonitoring.Scripts.CMProductionDataMonitoring import CMProductionDataMonitoring
# from Applications.Workflows.SVC.Scripts.RPA import RPA

from Applications.Workflows.ServiceTimeCard.RPA.Script.Main_Test_Script import Main_Test_Script
from Applications.Workflows.ServiceTimeCard.DocumentProcessing.Scripts.Main_Test_Script_DocumentProcessing import Main_Test_Script_DocumentProcessing
from Applications.Workflows.ServiceTimeCard.TaskCategorization.Script.Task_Categorization_Main_Test_Script import Task_Categorization_Main_Test_Script
from Applications.Workflows.QBSetup.Script.QB_main_test import QB_Setup


from Applications.Workflows.ErrorHospital.Scripts.ErrorHospital import ErrorHospital
from Applications.Workflows.NetsuiteReview.Scripts.NetsuiteReview850 import  NetsuiteReview850

from Applications.Workflows.ProcessTestFiles.Scripts.Process_Test_Files_Main import Process_Test_Files

class Execution:
    def __init__(self, username, team, task_type, lo):
        self.v_username = username
        self.v_task_type = task_type
        self.v_team = team
        self.lo = lo
    def main_execution(self):
        if self.v_task_type == "Production Data Monitoring":
            self.lo.log_to_file("INFO", "Executing Script Prodution Data Monitoring")
            pdm = ProductionDataMonitoring(self.v_task_type, self.lo, self.v_username)
            pdm.execute_main()

        elif self.v_task_type == "Document Processing Error":
            self.lo.log_to_file("INFO", "Executing Script Document Processing Error")
            dpe = Main_Test_Script_DocumentProcessing(self.v_task_type, self.lo, self.v_username)
            dpe.execute_main()

        elif self.v_task_type == "QB Setup":
            self.lo.log_to_file("INFO", "Executing Script Document Processing Error")
            dpe = QB_Setup(self.v_task_type, self.lo, self.v_username)
            dpe.execute_main()

        elif self.v_task_type == "Credit Memo Production Data Monitoring":
            self.lo.log_to_file("INFO", "Executing Script Credit Memo Prodution Data Monitoring")
            cmpdm = CMProductionDataMonitoring(self.v_task_type, self.lo, self.v_username)
            cmpdm.execute_main()
        elif self.v_task_type == "RPA":
            self.lo.log_to_file("INFO", "Executing Script for RPA")
            rpa = Main_Test_Script(self.v_task_type, self.lo, self.v_username)
            Main_Test_Script.execute_main(self)
        elif self.v_task_type == "Error Hospital":
            self.lo.log_to_file("INFO", "Executing Script Error Hospital")
            eh = ErrorHospital(self.v_task_type, self.lo, self.v_username)
            eh.execute_main()
        elif self.v_task_type == "Netsuite Review 850":
            self.lo.log_to_file("INFO", "Executing Script Error Hospital")
            nr = NetsuiteReview850(self.v_task_type, self.lo, self.v_username)
            nr.execute_main()
        elif self.v_task_type == "Process Test Files":
            self.lo.log_to_file("INFO", "Executing Script Process Test Files")
            ptf = Process_Test_Files(self.v_task_type, self.lo, self.v_username)
            ptf.execute_main()
        elif self.v_task_type == "Task Categorization":
            self.lo.log_to_file("INFO", "Executing Script Process Test Files")
            tc = Task_Categorization_Main_Test_Script(self.v_task_type, self.lo, self.v_username)
            tc.execute_main()

        else:
            self.lo.log_to_file('ERROR','Invalid Task Type')
