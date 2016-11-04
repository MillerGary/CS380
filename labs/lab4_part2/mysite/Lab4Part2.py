#import necessary packages
import sqlite3

#name the database file
sqlite_file = "db.sqlite3"

#establish a connection with the database
conn = sqlite3.connect(sqlite_file)

#set the connection as the value for the variable c
c = conn.cursor()

# sets the name of the table to be accessed
table = "film_album"

# sets the name of the attributes for each film to be added to the database

# film titles
film1 = "A New Hope"
film2 = "The Empire Strikes Back"
film3 = "Return of the Jedi"
film4 = "Goodfellas"
film5 = "The Godfather"

# Main Actors
actor1 = "Mark Hamill"
actor2 = "Robert De Niro"
actor3 = "Marlin Brando"

# Director's Name
director1 = "George Lucas"
director2 = "Martin Scorsese"
director3 = "Francis Ford Coppola"

# Genre
genre1 = "Science Fiction"
genre2 = "Crime/Drama"
genre3 = "Drama"

inserts = [(1, 'Mark Hamil', 'A New Hope', 'George Lucas', 'Science Fiction'),
           (2, 'Mark Hamil', 'The Empire Strikes Back', 'George Lucas', 'Science Fiction'),
           (3, actor1, film3, director1, genre1),
           (4, actor2, film4, director2, genre2),
           (5, actor3, film5, director3, genre3),
          ]


# test to make sure the database is connected properly
print("Check to make sure the database is properly connected")
c.execute("SELECT * from {tn}".format(tn=table))
for all_rows in c.fetchall():
   print(all_rows)

#drop table to avoid unique constraint failures
print("drop table to make sure no duplicate errors occur")
c.execute("DROP TABlE film_album")

#recreate table
c.execute("CREATE TABLE film_album ( 'id' integer NOT NULL PRIMARY KEY AUTOINCREMENT, 'main_actor' varchar(250) NOT NULL, 'film_title' varchar(250) NOT NULL, 'director_name' varchar(250) NOT NULL, 'genre' varchar(250) NOT NULL)")

print("Check to make sure table was dropped properly")
for row in c.execute("SELECT * FROM {tn}".format(tn=table)):
    print(row)

# Begin insert statements
c.executemany("INSERT INTO film_album VALUES (?, ?, ?, ?, ?)", inserts)
#c.execute("INSERT INTO {tn} (id, main_actor, film_title, director_name, genre) VALUES(3, {a}, {f}, {d}, {g})".format(tn=table, a=actor1, f=film1, d=director1, g=genre1))
#c.execute("INSERT INTO {tn} (id, main_actor, film_title, director_name, genre) VALUES(4, {a}, {f}, {d}, {g})".format(tn=table, a=actor1, f=film2, d=director1, g=genre1))
#c.execute("INSERT INTO {tn} (id, main_actor, film_title, director_name, genre) VALUES(5, {a}, {f}, {d}, {g})".format(tn=table, a=actor1, f=film3, d=director1, g=genre1))
#c.execute("INSERT INTO {tn} (id, main_actor, film_title, director_name, genre) VALUES(6, {a}, {f}, {d}, {g})".format(tn=table, a=actor2, f=film4, d=director2, g=genre2))
#c.execute("INSERT INTO {tn} (id, main_actor, film_title, director_name, genre) VALUES(7, {a}, {f}, {d}, {g})".format(tn=table, a=actor3, f=film5, d=director3, g=genre3))

#test the insert
for row in c.execute("SELECT * FROM {tn}".format(tn=table)):
    print(row)

# save the changes made to the database
conn.commit()

# close the connection with the database
conn.close()




