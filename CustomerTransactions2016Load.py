import pandas as pd
import pyodbc
import datetime as dt

df = pd.read_csv(
                 r"C:\WRHWorkshop\wsbwarehousefiles\CustomerTransactions2016.txt"
                )

df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])
df['LastEditedWhen'] = pd.to_datetime(df['LastEditedWhen'])
df['FinalizationDate'] = pd.to_datetime(df['FinalizationDate'])
df = df.fillna(value = 0  )

server = 'sqlvm9999'
database = 'DestinationDatabase'
cnxn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes')
cursor = cnxn.cursor()

for index,row in df.iterrows():
    cursor.execute("INSERT INTO raw.CustomerTransactions2016(CustomerTransactionID,CustomerID,TransactionTypeID,InvoiceID,PaymentMethodID,TransactionDate,AmountExcludingTax,TaxAmount,TransactionAmount,OutstandingBalance,FinalizationDate,IsFinalized,LastEditedBy,LastEditedWhen)\
                   values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)"\
                   ,row.CustomerTransactionID,row.CustomerID,row.TransactionTypeID,row.InvoiceID,row.PaymentMethodID,row.TransactionDate,row.AmountExcludingTax,row.TaxAmount,row.TransactionAmount,row.OutstandingBalance,row.FinalizationDate,row.IsFinalized,row.LastEditedBy,row.LastEditedWhen)
cnxn.commit()
cursor.close()
