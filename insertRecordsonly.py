import mysql.connector

# connect to database
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Super7898$$#",
    database="serviceDB"
)

cursorObject = dataBase.cursor()
print("enter new service")
new=input()
#  correct SQL syntax and parameter style
records = "INSERT INTO tbl_service (Services) VALUES (%s)"
val = (new,)  # must be a tuple

cursorObject.execute(records, val)
dataBase.commit()
print("Data inserted into tbl_service successfully")
