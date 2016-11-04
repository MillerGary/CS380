#import necessary packages
import sqlite3

#name the database file
sqlite_file = "campus_ii.sqlite3"

#establish a connection with the database
conn = sqlite3.connect(sqlite_file)

#set the connection as the value for the variable c
c = conn.cursor()

# set values for table to be queried
table1 = "course"
table2 = "department"
table3 = "instructor"
table4 = "student"
table5 = "takes"
table6 = "teaches"

# set values for each of the columns in the table
column1 = "ID"
column2 = "name"
column3 = "student"
column4 = "deptName"
column5 = "salary"
column6 = "title"
column6 = "CourseId"
column7 = "year"

print("SELECT * FROM instructor WHERE name = \"Nelson\";")
c.execute('SELECT * FROM {tn} WHERE {cn}="Nelson"'.format(tn=table3, cn=column2))
output = c.fetchall()
print(output)

print("\nSELECT name FROM instructor WHERE student = \"S1\";")
c.execute('SELECT {cn} FROM {tn} WHERE {cn2}="S1"'.format(tn=table3, cn=column2, cn2=column3))
output = c.fetchall()
print(output)

print("\nSELECT COUNT(ID) FROM takes;")
c.execute('SELECT COUNT({cn}) FROM {tn}'.format(tn=table5, cn=column1))
output = c.fetchall()
print(output)

print("\nSELECT * FROM course WHERE title like \"CS3%\";")
c.execute('SELECT * FROM {tn} WHERE {cn} like "CS3%"'.format(tn=table1, cn=column6))
output = c.fetchall()
print(output)

print("\nSELECT DISTINCT(deptName) FROM department;")
c.execute('SELECT DISTINCT({cn}) FROM {tn}'.format(tn=table2, cn=column4))
output = c.fetchall()
print(output)

print("\nSELECT name, ID FROM student;")
c.execute('SELECT {cn2}, {cn} FROM {tn}'.format(tn=table4, cn=column1, cn2=column2))
output = c.fetchall()
print(output)

print("\nSELECT courseId FROM teaches WHERE year = \"2009\";")
c.execute('SELECT DISTINCT({cn}) FROM {tn} WHERE {cn2} = ("2009")'.format(tn=table6, cn=column6, cn2=column7))
output = c.fetchall()
print(output)

print("\nShow Faber's current salary")
# show current salary
c.execute('SELECT {cn}, {cn2} FROM {tn} WHERE {cn} == "Farber"'.format(tn=table3, cn=column2, cn2=column5))
output = c.fetchall()
print(output)
print("Updating Faber's salary to be 101")
#UPDATE instructor SET salary == "101" WHERE name == "Farber";
c.execute('UPDATE {tn} SET {cn2} == "101" WHERE {cn} == "Farber"'.format(tn=table3, cn=column2, cn2=column5))
# show the change in salary
print("Showing the change was successful")
c.execute('SELECT {cn}, {cn2} FROM {tn} WHERE {cn} == "Farber"'.format(tn=table3, cn=column2, cn2=column5))
output = c.fetchall()
print(output)

#close connection with the database
conn.close()
