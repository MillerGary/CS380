#!/usr/bin/env python
# 13 Oct 2016
# Written by Oliver Bonham-Carter following the tutorial at:
# http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
# email: obonhamcarter@allegheny.edu

# runs, "select * from instructor;" using python

sqlite_file = "campus_iii.sqlite3" # the database file.

import sqlite3
conn = sqlite3.connect(sqlite_file) # load the database file, defined above
c = conn.cursor()

c.execute("SELECT * FROM instructor")
row = c.fetchall()
for line_list in row:
	print "\nline_list = ",line_list,type(line_list)
#line_list =  (u'10114', u'Maximillian', u'S5', u'Biology', 86000) <type 'tuple'>
	count = 0
	for i in line_list:
		count = count + 1
		print "  Tuple Position in line_list :", count,"::",i
conn.close() 

# If we are finished with our operations on the database file, 
# we have to close the connection


