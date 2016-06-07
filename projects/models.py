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

	def get_short_description(self):
		return self.description[:20]

class Project(models.Model):
	name = models.CharField(max_length=50)
	alias = models.CharField(max_length=10)
	description = models.TextField(max_length= 200)
	#status = models.OneToOneField( Status )
	status =  models.ForeignKey(Status)
	user = models.ForeignKey(User)
	create_at = models.DateField( default = datetime.now )
	dead_line = models.DateField()
	path = models.CharField(max_length = 50)

	def __str__(self):
		return self.name

	def validate_unique(self, *args, **kwargs):
		super(Project, self).validate_unique(*args, **kwargs)
		if Project.objects.filter(path = self.path).exists():
			raise ValidationError({'path':['El path debe se ser unico',]})

	def save(self, force_insert = False, force_update = False):
		self.path = self.alias.replace(" ", "_").lower()
		super(Project, self).save(force_insert, force_update)

