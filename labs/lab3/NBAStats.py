#!/usr/bin/python
#used to import sqlite3 into the phyton library
import sqlite3

print "Attempting to connect to database"
#connects to sqlite3 database
conn = sqlite3.connect('NBAStats.sqlite3')

print "Opened database successfully"
#insert the first four rookies into the database
print "Inserting the top four rookies drafted for this upcoming season"
#statements can only be executed once otherwise error occurs
#conn.execute("INSERT INTO Player (ID, Name, Team, Position, Age) VALUES (498, 'Ben Simmons', 'Philadelphia', 'SF', 20)");

#conn.execute("INSERT INTO Player (ID, Name, Team, Position, Age) VALUES (499, 'Brandon Ingram', 'LA Lakers', 'SF', 19)");

#conn.execute("INSERT INTO Player (ID, Name, Team, Position, Age) VALUES (500, 'Jaylen Brown', 'Boston', 'SF', 19)");

#conn.execute("INSERT INTO Player (ID, Name, Team, Position, Age) VALUES (501, 'Dragan Bender', 'Phoenix', 'PF', 18)");
#commit changes to database
#conn.commit()

print "Records created successfully";
#this statement intentionally violates the integrity constraints, causes error if uncommented
#conn.execute("INSERT INTO Player (ID, Name, Team, Position, Age) VALUES ('501', 'Kris Dunn', 'Minnesota', 'PG', 22)");

#conn.commit()

print "Record was not successfully created"

print "Selecting rookies to show they were successfully inserted"
#select statement #1
cursor = conn.execute("SELECT ID, Name FROM Player WHERE ID > 497")
for row in cursor:
    print "ID: ", row[0]
    print "Name: ", row[1], "\n"

print "Deleting last inserted record from the database"
#select statement #2
cursor = conn.execute("SELECT COUNT(ID) FROM Player")
for row in cursor:
    print row[0], "\n"
#delete statement
conn.execute("DELETE FROM Player WHERE ID == 500;")
#commit the delete statement to database
conn.commit()

print "Show that the record was successfully deleted"
#select statement #3
cursor = conn.execute("SELECT COUNT(ID) FROM Player")
for row in cursor:
    print "Number of players :", row[0], "\n"

print "Updating Kevin Durant's team to be Miami"

print "Data before the update statement: "

#Must set team back to OKC each time otherwise UPDATE will
#only sucessfully reflect changes after the first execution of the program
conn.execute("UPDATE Player set Team == 'Okc' WHERE Name == 'Kevin Durant'")
conn.commit()

cursor = conn.execute("SELECT Name, Team FROM Player WHERE Name == 'Kevin Durant'")
for row in cursor:
    print "Player Name: ", row[0]
    print "Team: ", row[1], "\n"

print "Data after the update statement: "

#update statement
conn.execute("UPDATE Player set Team == 'Mia' WHERE Name == 'Kevin Durant'")
#commit the update change to the database
conn.commit()
#select statement #4
cursor = conn.execute("SELECT Name, Team FROM Player WHERE Name == 'Kevin Durant'")
for row in cursor:
    print "Player Name: ", row[0]
    print "Team: ", row[1], "\n"

print "Update was done successfully"

print "Printing players who average more than 25 points per game"
#select statement #5
cursor = conn.execute("SELECT Name, PPG FROM Player WHERE PPG > 25")
for row in cursor:
    print "name: ", row[0]
    print "PPG: ", row[1], "\n"

print "Selecting all teams from the western conference"
#select statement #6
cursor = conn.execute("SELECT TeamName FROM Team WHERE Conference == 'West'")
for row in cursor:
    print "Team name: ", row[0]

print "Selecting all teams that achieved more than 50 wins"
#select statement #7
cursor = conn.execute("SELECT TeamName, Win FROM Team WHERE Win > 50")
for row in cursor:
    print "Team name: ", row[0]
    print "Wins: ", row[1], "\n"

print "Select Players and their Team name who average more than 25 points per game and played in the Western conference"
#select statement #8
cursor = conn.execute("SELECT Player.Name, Player.PPG, Team.TeamName, Team.Conference FROM Player, Team WHERE Player.Team = Team.TeamName AND Team.Conference = 'West' AND Player.PPG > 25")
for row in cursor:
    print "Player name: ", row[0]
    print "Player's PPG: ", row[1]
    print "Player's team: ", row[2]
    print "Team's conference: ", row[3], "\n"

print "Selecting teams from the Eastern conference group by least amount of wins to most"
#select statement #9
cursor = conn.execute("SELECT TeamName, Win FROM Team WHERE Conference = 'East' GROUP BY Win")
for row in cursor:
    print "Team Name:", row[0], " Wins:", row[1], "\n"

print "Selecting the top 20 players in the NBA with respect to versatility index"
#select statement #9
cursor = conn.execute("SELECT Player.Name, Player.VI FROM Player GROUP BY VI ORDER BY VI DESC LIMIT 20")
for row in cursor:
    print "Player Name: ", row[0], " VI Index: ", row[1], "\n"

print "Operation done successfully"
#close connection to the database
conn.close()
