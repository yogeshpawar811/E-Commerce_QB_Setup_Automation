
# conn = psycopg2.connect(database="SPSCommerce", user="postgres", password="admin", host="127.0.0.1", port="5432")

import psycopg2 as dbconn
import pandas as pd
import io

class CreateDashboard:

    def convert_to_csv(self, v_csv_path,v_excel_path ):
        data_xls = pd.read_excel(v_excel_path, 'Sheet1', index_col=None)
        data_xls.to_csv(v_csv_path, encoding='utf-8')

    def writetopostgres(self, f,tablenm):
        conn = dbconn.connect("postgresql://postgres:admin@127.0.0.1/postgres")
        cursor = conn.cursor()
        #cursor.execute('create table BCM_DATAS (Id text, Request_Type text, Supplier_Name text, Number_of_retailers int, Execution_time float);COMMIT; ')
        cursor.copy_from(f, tablenm, columns=('ID', 'REQUEST_TYPE', 'SUPPLIER_NAME', 'NUMBER_OF_RETAILERS', 'EXECUTION_TIME'), sep=',')
        cursor.close()


cd = CreateDashboard()
v_csv_path = "D:\Business_Data\AutomationReports\BCM\BCM-July18.csv"
v_excel_path = "D:\Business_Data\AutomationReports\BCM\BCM-July18.xlsx"
#csv = cd.convert_to_csv(v_csv_path, v_excel_path)
#Let's read only the columns we need with usecols
df = pd.read_csv(v_csv_path)

#load data in a temporary csv file
f = io.StringIO()
df.to_csv(f, index=False, header=False, sep=',')
f.seek(0)
tableNm = 'BCM_RECORDS'
#write to Postgres by sending our temporary csv f to copy
cd.writetopostgres(f, tableNm)
print("done")