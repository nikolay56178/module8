from peewee import *
from datetime import date

conn = SqliteDatabase('ansver_orm.sqlite')

class Students(Model):
	id = PrimaryKeyField(IntegerField())
	name = CharField()
	surname = CharField()
	age = IntegerField()
	city = CharField()
	class Meta:
		database = conn

class Courses(Model):
	id = PrimaryKeyField(IntegerField())
	name = CharField()
	time_start = DateField ()
	time_end = DateField ()
	class Meta:
		database = conn

class Students_Courses(Model):
	students_id = ForeignKeyField(Students, backref= 'Students_Courses')
	courses_id = ForeignKeyField(Courses, backref= 'Students_Courses')
	class Meta:
		database = conn

Students.create_table()
Courses.create_table()
Students_Courses.create_table()

# s1 = Students.create(id = 1,name = 'Max',surname = 'Brooks',age = 24,city = 'Spb')
# s2 = Students.create(id = 2,name = 'John',surname = 'Stones',age = 15,city = 'Spb')
# s3 = Students.create(id = 3,name = 'Andy',surname = 'Wings',age = 45,city = 'Manhester')
# s4 = Students.create(id = 4,name = 'Kate',surname = 'Brooks',age = 34,city = 'Spb')

#c1 = Courses.create(id = 1, name = 'python', time_start = '21.07.21', time_end = '21.08.21')
#c2 = Courses.create(id = 2, name = 'java', time_start = '13.07.21', time_end = '16.08.21')

# sc1 = Students_Courses.create(students_id = 1, courses_id = 1)
# sc2 = Students_Courses.create(students_id = 2, courses_id = 1)
# sc3 = Students_Courses.create(students_id = 3, courses_id = 1)
# sc4 = Students_Courses.create(students_id = 4, courses_id = 2)

for i in Students.select().where(Students.age > 30):
	print(i.name, end=' ')
print()
for j in Students.select().join(Students_Courses).where(Students_Courses.courses_id == 1):
	print(j.name, end=' ')
print()
for j in Students.select().join(Students_Courses).where(Students_Courses.courses_id == 1).where(Students.city == 'Spb'):
	print(j.name, end=' ')