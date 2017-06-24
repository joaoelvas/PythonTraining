from django.db import models

# Create your models here.

class Course(models.Model):
	# now is the now when an instance of this class is created
	# using the timezone of setting.py
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=255)
	description = models.TextField()

	def __str__(self):
		return self.title

class Step(models.Model):
	"""docstring for ClassName"""
	title = models.CharField(max_length=255)
	description = models.TextField()
	content = models.TextField(blank=True, default='')
	order = models.IntegerField(default=0)
	course = models.ForeignKey(Course)

	class Meta:
		# This will cause the model to be ordered by field1, then field2 
		# if there are any conflicts on field1 (two instances having the 
		# same field1 value). Finally, they'll be sorted by id if a conflict still exists.
		# ordering = ['field1', 'field2']
		ordering = ['order',]
		
	def __str__(self):
		return self.title
