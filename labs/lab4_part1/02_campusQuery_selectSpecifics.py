#!/usr/bin/env python
# 13 Oct 2016
# Written by Oliver Bonham-Carter following the tutorial at
# http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
# email: obonhamcarter@allegheny.edu

# runs, "select * from instructor;" using python

import sqlite3

sqlite_file = "campus_ii.sqlite3" # the database file.

table_name = 'instructor'   # name of the table to be queried
id_column = 'ID'
some_id = 10110
column_2 = 'name'
column_3 = 'student'

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


########################################################################################
# 1) Contents of all columns for row that match a certain value in 1 column
# select * from instructor where name = "Nelson";
# Output:
# 10111|Nelson|S5|CompBio|103000

c.execute('SELECT * FROM {tn} WHERE {cn}="Nelson" '.format(tn=table_name, cn=column_2))
all_rows = c.fetchall()
print('1):', all_rows)



########################################################################################
# 2) Value of a particular column for rows that match a certain value in column_1
# select name from instructor where student ="S1";
# Output:
# Miller
# Johnson
# Wu


c.execute('SELECT ({attrib}) FROM {tn} WHERE {c}="S1"' .format(attrib=column_2, tn=table_name, c=column_3))
all_rows = c.fetchall()
print('2):', all_rows)




########################################################################################

# 3) Value of 2 particular columns for rows that match a certain value in 1 column
# select name, student from instructor where name == "Watson";
# Output:
# Watson|S4

c.execute('SELECT {attrib1},{attrib2} FROM {tn} WHERE {attrib1}="Watson"'.format(attrib1=column_2, attrib2=column_3, tn=table_name, cn=column_2))
all_rows = c.fetchall()
print('3):', all_rows)

########################################################################################

# 4) Selecting only up to three rows that match a certain value in 1 column
# SELECT * FROM instructor where ID like "101%" limit 3;
# Output:
# 10101|Miller|S1|CompSci|95000
# 10102|Johnson|S1|CompSci|95400
# 10103|Charleson|S2|CompSci|96000

c.execute('SELECT * FROM {tn} WHERE {attrib1} like "101%" limit 3'.format(tn=table_name, attrib1="Id"))
three_rows = c.fetchall()
print('4):', three_rows)


########################################################################################

# 5) Selecting names where the double-l is two letters in from both end.
# SELECT * FROM instructor where Name like "__ll__";
# Output:
# 10101|Miller|S1|CompSci|95000

c.execute('SELECT * FROM {tn} WHERE {attrib1} like "__ll__"'.format(tn=table_name, attrib1=column_2))
ll_rows = c.fetchall()
print('5):', ll_rows)


########################################################################################


# 6) Check if a certain ID exists and print its column contents
# select * from instructor where Id ="10110";
# Output:
# 10110|Watson|S4|CompSci|100500



c.execute("SELECT * FROM {tn} WHERE {idf}={my_id}".format(tn=table_name, cn=column_2, idf=id_column, my_id=some_id))
id_exists = c.fetchone()

if id_exists:
    print('6): {}'.format(id_exists))
else:
    print('6): {} does not exist'.format(some_id))


# 7) Check if a certain ID exists and print its column content if so,
#    otherwise, print out that the id does not exist
# select * from instructor where Id ="007";
# Output:
# - nothing -

some_id = "007"
c.execute("SELECT * FROM {tn} WHERE {idf}={my_id}".format(tn=table_name, cn=column_2, idf=id_column, my_id=some_id))
id_exists = c.fetchone()

if id_exists:
    print('7): {}'.format(id_exists))
else:
    print('7): {} does not exist'.format(some_id))


# 8) change an entry using UPDATE.

# 10112|Farber|S5|CompBio|101000
# UPDATE instructor set salary == "101" where name == "Farber";
# 10112|Farber|S5|CompBio|101

# Check Farber's salary before...
c.execute('SELECT * FROM {tn} WHERE {attrib1} = "Farber"'.format(tn=table_name, attrib1=column_2))
f_rows = c.fetchall()
print('8):', f_rows)

c.execute('UPDATE {tn} set salary = "101" where {attrib1} = "Farber"'.format(tn=table_name, attrib1=column_2))
f_rows = c.fetchall()
print('9):', f_rows)


# Check Farber's salary after...
c.execute('SELECT * FROM {tn} WHERE {attrib1} = "Farber"'.format(tn=table_name, attrib1=column_2))
f_rows = c.fetchall()
print('10):', f_rows)

# Committing changes and closing the connection to the database file
conn.commit()

# set the whole record back to its original values.
c.execute('UPDATE {tn} set salary = "101000" where {attrib1} = "Farber"'.format(tn=table_name, attrib1=column_2))
f_rows = c.fetchall()
print('11):', f_rows)


# Check Farber's salary after...
c.execute('SELECT * FROM {tn} WHERE {attrib1} = "Farber"'.format(tn=table_name, attrib1=column_2))
f_rows = c.fetchall()
print('12):', f_rows)

# Committing changes and closing the connection to the database file
conn.commit()







# Closing the connection to the database file
conn.close()

