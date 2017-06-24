from courses.models import Course

c = Course()
c.title = "Python Basics"
c.description = "Learn the basics of Python"
c.save()
Course.objects.all()

Course(title="Python Collections", description="Learn about list, dict, and tuple").save()
Course.objects.all()

Course.objects.create(title="Object-Oriented Python", description="Learn about Python's classes")
Course.objects.all()

# https://docs.djangoproject.com/en/1.8/topics/db/queries/#retrieving-objects