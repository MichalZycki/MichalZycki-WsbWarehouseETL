import pandas as pd
import pyodbc
import datetime as dt

df = pd.read_csv(
                 r"C:\Users\michalzycki\Desktop\wrh\pliki\wsbwarehousefiles\CustomerTransactions2019.txt"
                )

df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])
df['LastEditedWhen'] = pd.to_datetime(df['LastEditedWhen'])
df['FinalizationDate'] = pd.to_datetime(df['FinalizationDate'])
df = df.fillna(value = 0  )

server = 'vmpythonwrh'
database = 'DestinationWarehouse'
username = 'michalzycki'
password = '123456Qqwsd12345@'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

for index,row in df.iterrows():
    cursor.execute("INSERT INTO raw.CustomerTransactions2019(CustomerTransactionID,CustomerID,TransactionTypeID,InvoiceID,PaymentMethodID,TransactionDate,AmountExcludingTax,TaxAmount,TransactionAmount,OutstandingBalance,FinalizationDate,IsFinalized,LastEditedBy,LastEditedWhen)\
                   values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)"\
                   ,row.CustomerTransactionID,row.CustomerID,row.TransactionTypeID,row.InvoiceID,row.PaymentMethodID,row.TransactionDate,row.AmountExcludingTax,row.TaxAmount,row.TransactionAmount,row.OutstandingBalance,row.FinalizationDate,row.IsFinalized,row.LastEditedBy,row.LastEditedWhen)
cnxn.commit()
cursor.close()