import pyodbc

def OpenConnection():
    try:
        con = pyodbc.connect('Driver={SQL Server};'
                      'Server=II31-2KQX0X2\SQLEXPRESS;'
                      'Database=python_db;'
                      'Trusted_Connection=yes;')
    except Exception as exp:
        print(exp)
    return con

def CloseConnection(con):
    try:
        con.close()
    except Exception as exp:
        print(exp)

connection = OpenConnection()
cursor = connection.cursor()
cursor.execute("select * from Doctor")
for row in cursor:
    print(row)

CloseConnection(connection)