import sqlite3
from datetime import datetime

conn = sqlite3.connect('ansver.sqlite')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Students(
	id int PRIMARY KEY NOT NULL, 
	name Varchar(32),
	surname Varchar(32),
	age int,
	city Varchar(32)
)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS Courses(
	id int PRIMARY KEY NOT NULL,
	name Varchar(32),
	time_start datetime,
	time_end datetime
)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS Students_Courses (
	student_id int NOT NULL REFERENCES Students(id),
	course_id int NOT NULL REFERENCES Courses(id)
	)""")	
									
# cursor.executemany('''INSERT INTO Courses VALUES (?,?,?,?)''',[
# 	(1, 'python', '21.07.21', '21.08.21'),
# 	(2, 'java', '13.07.21', '16.08.21')
# 	 ])

# cursor.executemany('''INSERT INTO Students VALUES (?,?,?,?,?)''',[
# 	(1, 'Max', 'Brooks', 24, 'Spb'),
# 	(2, 'John', 'Stones', 15, 'Spb'),
# 	(3, 'Andy', 'Wings', 45, 'Manhester'),
# 	(4, 'Kate', 'Brooks', 34, 'Spb')
# 	])
# cursor.executemany('''INSERT INTO Students_Courses VALUES (?,?)''',[
# 	(1, 1),
# 	(2, 1),
# 	(3, 1),
# 	(4, 2)
# 	])
conn.commit()

cursor.execute('''SELECT Students.name FROM Students WHERE age > 30''')
print(cursor.fetchall())


cursor.execute('''SELECT Students.name FROM Students JOIN Students_Courses ON Students.id = Students_Courses.student_id
			JOIN Courses ON Courses.id = Students_Courses.course_id
			WHERE Courses.name = 'python'
	''')
print(cursor.fetchall())

cursor.execute('''SELECT Students.name FROM Students JOIN Students_Courses ON Students.id = Students_Courses.student_id
			JOIN Courses ON Courses.id = Students_Courses.course_id
			WHERE Courses.name = 'python' and Students.city = 'Spb'
	''')
print(cursor.fetchall())
 
