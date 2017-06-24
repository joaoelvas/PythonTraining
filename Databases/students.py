from peewee import *

db = SqliteDatabase('students.db') # SqliteDatabase - The class from Peewee that lets us connect to an SQLite database

class Student(Model):
	"""docstring for Student"""
	username = CharField(max_length=255, unique=True)
	points = IntegerField(default=0)

	class Meta:
		database = db

students = [
	{'username': 'kennethlove',
	'points': 14718},
	{'username': 'chalkers',
	'points': 11912},
	{'username': 'joykesten2',
	'points': 7363},
	{'username': 'craigsdennis',
	'points': 4079},
	{'username': 'davemcfarland',
	'points': 14717},
]

def add_students():
	for student in students:
		try:
			Student.create(username=student['username'], points=student['points'])
		except IntegrityError:
			student_record = Student.get(username=student['username'])
			student_record.points = student['points']
			student_record.save()

# orders by points in descending order and then takes the first one
# first one is the one with more points
def top_student():
	student = Student.select().order_by(Student.points.desc()).get()
	return student
		

if __name__ == '__main__':
	db.connect()
	db.create_tables([Student], safe=True)
	add_students()
	print("Our top student right now is: {0.username}.".format(top_student()))


# http://peewee.readthedocs.io/en/latest/peewee/querying.html
# .create() - creates a new instance all at once
# .select() - finds records in a table
# .save() - updates an existing row in the database
# .get() - finds a single record in a table
# .delete_instance() - deletes a single record from the table
# .order_by() - specify how to sort the records