import pyodbc,json

# Sample code for connecting Azure SQL DB from Python and creating a key value dictionary 
# Pre requisite install pyodbc module & MS SQL ODBC driver 


server = 'mssqlserver535.database.windows.net' 
driver= '{ODBC Driver 13 for SQL Server}'
database = 'MSQLIOT535' 

username = input("Please enter DB Userid: ") 
password = input("Please enter DB Password: ")

dbstring= 'DRIVER='+driver+';SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password
print("DB String :- " + dbstring)
cnxn = pyodbc.connect(dbstring)
cursor = cnxn.cursor()
cursor.execute("select * from dbo.tbl_IOT")

#Getting the DB table headers & Rows from cursor dscription and loading it in a array
columns = []
for item in cursor.description:
        columns.append(item[0])

rows = cursor.fetchall()

#Creating a key value pair by combining two arrays and converting it into a dictionary
#Zip to combine two array of header & each rows  & dict to convert array to dictionary
filewrite = open("newfile.txt",'a')
for eachrow in rows:
    mydict=dict(zip(columns,eachrow))   
    filewrite.writelines(str(mydict))
    filewrite.writelines("\n")
filewrite.close()

fileread = open("newfile.txt",'r')
for lines in fileread.readlines():
    print(lines)
fileread.close()

