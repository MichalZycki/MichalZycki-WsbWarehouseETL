import pandas as pd
import pyodbc
import datetime as dt

df = pd.read_csv(
                 r"C:\Users\michalzycki\Desktop\wrh\pliki\wsbwarehousefiles\DateTable.txt"
                )

server = 'vmpythonwrh'
database = 'DestinationWarehouse'
username = 'michalzycki'
password = '123456Qqwsd12345@'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

for index,row in df.iterrows():
    cursor.execute("INSERT INTO raw.DateTable(ID,TheDate,TheDay,TheDayName,TheWeek,TheISOWeek,TheDayOfWeek,TheMonth,TheMonthName,TheQuarter,TheYear,TheFirstOfMonth,TheLastOfYear,TheDayOfYear)\
                   values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)"\
                   ,row.ID,row.TheDate,row.TheDay,row.TheDayName,row.TheWeek,row.TheISOWeek,row.TheDayOfWeek,row.TheMonth,row.TheMonthName,row.TheQuarter,row.TheYear,row.TheFirstOfMonth,row.TheLastOfYear,row.TheDayOfYear)
cnxn.commit()
cursor.close()