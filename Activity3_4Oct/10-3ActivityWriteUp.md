# October 3rd Class Participation Exercise

+ Gary Miller

## Discussion Questions

+ By opening the database file in the db browser program the main tab displays all of the tables that exist within the database. These tables include course, department, instructor, student, takes, and teaches.

+ Under the same database strcuture tab that displayed that tables within the databse, it is possible to see the schema of each of the tables in thise database. Alternatively the .schema command can be entered by running sqlite3 in the terminal and it will output the schema of each of the table that can be easily copy and pasted into another document. The schema of the table were of the the following:

	CREATE TABLE instructor (
		ID    char(5),
		name    varchar(20) not null,
		student varchar(20) not null,
		deptName    varchar(20),
		salary    numeric(8,2),
		primary key (ID),
		foreign key (deptName) references department
	);
	CREATE TABLE student (
		ID    varchar(5),
		name    varchar(20) not null,
		deptName    varchar(20),
		totCred     numeric(3,0),
		primary key (ID),
		foreign key (deptName) references department
	);
	CREATE TABLE course (
		courseId    varchar(8) primary key,
		title        varchar(50),
		deptName    varchar(20),
		credits       numeric(2,0),
		foreign key (deptName) references department);
		CREATE TABLE department (
		courseId varchar(8) primary key,
		courseType varchar(8),
		deptName varchar(8)
	);
	CREATE TABLE takes (
		ID char(5) NOT NULL,
		courseId varchar(8)  NOT NULL,
		secId varchar(8) NOT NULL,
		semester varchar(8)  NOT NULL,
		year int NOT NULL,
		grade text NOT NULL);
		CREATE TABLE teaches (
		ID    char(5) primary key,
		courseId varchar(8),
		secId varchar(8),
		semester varchar(8),
		year varchar(8)
	);

+ By entering following the query: 
		
		SELECT courseID FROM course INTERSECT SELECT courseID FROM department;
The output gives the courseID for each course tha is common to both the course table and the department table. The output of this query shows that CS100, CS200, and CS601 are common to both tables.

+ In order to list all of the instructors and the students with whom are working with one another the following query was enterred:

		select instructor.name, student.name from instructor inner join student on student.ID = student;

The output of this query returned the names of all the instrucors and students that arw roking together and gave the following list of student instructor pairs:
	
		"Miller"	"Michaels"
		"Johnson"	"Michaels"
		"Charleson"	"Peterson"
		"Thompson"	"Peterson"
		"Mauler"	"Mullen"
		"Jackson"	"Mullen"
		"Chesterfield"	"Mullen"
		"Jenkins"	"Scotts"
		"William"	"Scotts"
		"Wu"		"Michaels"

+ In order to get a similar query as the previous one except the depetmant name of the instrcutor should be included as well, the query was changed to:

		select instructor.name, instructor.deptName, student.name from instructor inner join student on student.ID = student;

The output of the new query was as follows:

		"Miller"	"CompSci"	"Michaels"
		"Johnson"	"CompSci"	"Michaels"
		"Charleson"	"CompSci"	"Peterson"
		"Thompson"	"CompSci"	"Peterson"
		"Mauler"	"Math"		"Mullen"
		"Jackson"	"CompSci"	"Mullen"
		"Chesterfield"	"CompBio"	"Mullen"
		"Jenkins"	"CompBio"	"Scotts"
		"William"	"Math"		"Scotts"
		"Wu"		"Math"		"Michaels"

+ In order to create a view table composed of instructors, their department name, and the name of the students that they are working with, the following query was entered:

		create view iSViewTable as select instructor.name, instructor.deptName, student.name from instructor inner join student on student.ID = student;

+ In order to drop the view table that was created in the previous query, the following query was entered:

		drop table iSViewTable;

+ In order to find all of the CS courses that exist in the teaches table the following query was used:

		select * from teaches where courseID like 'CS____';

The underscore allow for ambigious matching therefore any course id that matches CS with any four charcaters after will yield a match. the output of the query was as follows:

		"123461"	"CS-101"	"1"	"Fall"		"2014"
		"123462"	"CS-101"	"1"	"Fall"		"2014"
		"12347"		"CS-201"	"1"	"Spring"	"2014"
		"123481"	"CS-104"	"2"	"Spring"	"2016"
		"1234821"	"CS-105"	"2"	"Summer"	"2016"
		"1234821a"	"CS-106"	"2"	"Summer"	"2016"
		"1234821b"	"CS-107"	"2"	"Summer"	"2016"
		"1234822"	"CS-108"	"2"	"Summer"	"2016"
		"1234823"	"CS-109"	"2"	"Summer"	"2016"
		"12349"		"CS-401"	"1"	"Fall"		"2009"






