from django.db import models
from django.conf import settings
from datetime import date


class Person(models.Model):

	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,primary_key=True,)
	name = models.CharField(max_length=50)
	surname = models.CharField(max_length=50)
	is_teacher = models.BooleanField(default=False)
	def __str__(self):
		return '{} {}'.format(self.name, self.surname)


class Connection(models.Model):

	teacher = models.ForeignKey(Person,related_name='connection_teacher', on_delete=models.CASCADE, limit_choices_to={'is_teacher': True})
	student = models.ForeignKey(Person,related_name='connection_student', on_delete=models.CASCADE ,limit_choices_to={'is_teacher': False})
	def __str__(self):
		return '{} {}'.format(self.teacher, self.student)

class Homework(models.Model):

	connection = models.ForeignKey(Connection,related_name='homework', on_delete=models.CASCADE)
	text = models.CharField(max_length=50)
	def __str__(self):
		return '{}'.format(self.connection.student)

'''
for m in range(len(meeting_sala_day)-1):
	if timedelta(meetings[m].date, meetings[m+1].date) > 1.5h 
'''

class MeetingManager(models.Manager):
	def next(self):
		return self.filter(date__range=[date.today(), "2020-01-31"])[0]
	def last(self):
		return self.filter(date__range=["2018-01-31", date.today()])[0]

class Meeting(models.Model):
	
	connection = models.ForeignKey(Connection,related_name='meeting', on_delete=models.CASCADE)
	date = models.DateTimeField()
	objects = MeetingManager()

	def __str__(self):
		return '{}'.format(self.connection)

