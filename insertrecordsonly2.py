import mysql.connector

# Connect to the database
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="customerdb"
)

cursorObject = dataBase.cursor()

# Correct SQL syntax
records = "INSERT INTO users (Id, Username, Email) VALUES (%s, %s, %s)"
value = (1, 'John Doe', 'johndoe@yahoo.com')  # single tuple

cursorObject.execute(records, value)

# Commit changes
dataBase.commit()

print("Data inserted into table successfully.")