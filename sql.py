import sqlite3
connection = sqlite3.connect("student.db")

cursor = connection.cursor()

table_info = """
Create table STUDENT(NAME VARCHAR(25) ,CLASS VARCHAR(25),
SECTION VARCHAR(25) ,MARKS INT);
"""
cursor.execute(table_info)
cursor.execute('''Insert into STUDENT values('Abhi','Data Science','A','95')''')
cursor.execute('''Insert into STUDENT values('Pradeep','Data Science','A','87')''')
cursor.execute('''Insert into STUDENT values('Chetan','Data Science','B','100')''')
cursor.execute('''Insert into STUDENT values('Belo','SDE','A','90')''')
cursor.execute('''Insert into STUDENT values('Rahul','DEVOPS','B','60')''')
cursor.execute('''Insert into STUDENT values('Deepak','DEVOPS','A','58')''')

print("The inserted records are ")

data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

connection.commit()
connection.close()
