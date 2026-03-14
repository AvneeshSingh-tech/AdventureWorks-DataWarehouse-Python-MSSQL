import pyodbc

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=AVNEESHSINGH;"
    "DATABASE=MYFIRST_PYTHON_BANK_DW;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

cursor.execute("SELECT GETDATE()")

for row in cursor:
    print(row)
