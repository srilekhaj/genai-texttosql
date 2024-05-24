#responsible for creating db tables
import sqlite3

#coonnect to sqliite
connection = sqlite3.connect("student.db")

#create a cursor
#resposible for inserting retrieving record
cursor = connection.cursor()

#create a table
table_info = """
    CREATE TABLE STUDENT (NAME VARCHAR(255), CLASS VARCHAR(30), SECTION VARCHAR(30), MARKS INT);
"""

cursor.execute(table_info)
#Inserting records into the STUDENT table
cursor.execute('''INSERT INTO STUDENT VALUES('John Doe', '10th', 'A', 85)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Jane Smith', '11th', 'B', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Alice Johnson', '9th', 'C', 78)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Bob Williams', '12th', 'A', 95)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Emily Brown', '10th', 'B', 88)''')

print("the records are")

data = cursor.execute("SELECT * FROM STUDENT")

for row in data:
    print(row)


#closing the connection
connection.commit()
connection.close()