'''
@ Author - Karan Pandya
@ Creation date - 08/31/2018
@ Description - Calculate the total execution time and update the results in an google sheet.
'''

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from Utilites import AppConstants

class ReportFileUtility:

    def __init__(self, task_type):
        self.v_task_type = task_type
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(AppConstants.CLIENT_SECRET_JSON_FILE_PATH, scope)
        client = gspread.authorize(creds)
        sht = client.open("Framework Demo")
        self.G_sheet = sht.worksheet(task_type)
        values_list = self.G_sheet.col_values(1)
        Row_Count = len(values_list)
        self.Row_Count = Row_Count + 1


    def update_sheet(self, username, number_of_unit, execution_time, date):
        val = []
        val.append(username)
        val.append(number_of_unit)
        val.append(execution_time)
        val.append(date)
        self.G_sheet.append_row(val)
