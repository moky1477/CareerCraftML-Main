import sqlite3

## Connect to sqlite
connection = sqlite3.connect("student.db")

# Create a cursor obj to insert record, create table, retrieve
cursor = connection.cursor()

# Create the table

table_info = """
    CREATE TABLE STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT)
"""

cursor.execute(table_info)

# Insert some records

cursor.execute('''INSERT INTO STUDENT VALUES('Mokshit', 'Artificial Intelligence', 'B', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Yutee', 'Mechanical', 'D', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Sarthak', 'IT', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Rickin', 'E&TC', 'A', 90)''')

# Display all the records

print("The inserted rows are")

data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)


# Close the connection
connection.commit()
connection.close()