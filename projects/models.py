from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Status(models.Model):
	name = models.CharField(max_length=20)
	description = models.TextField(max_length= 100)
	color = models.CharField(max_length= 10)
	
	def __str__(self):
		return self.name

class Project(models.Model):
	name = models.CharField(max_length=50)
	alias = models.CharField(max_length=10)
	description = models.TextField(max_length= 200)
	#status = models.OneToOneField( Status )
	status =  models.ForeignKey(Status)
	user = models.ForeignKey(User)
	create_at = models.DateField( default = datetime.now )
	dead_line = models.DateField()

	def __str__(self):
		return self.name