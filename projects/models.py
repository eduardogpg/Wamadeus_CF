from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.

def upload_location(instance, filename):
	filebase, extension = filename.split(".")
	return "image_project/%s/%s.%s" % (instance.id, instance.id, extension)

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
	image = models.ImageField( upload_to=upload_location, null = True, blank=True )

	def __str__(self):
		return self.name

	#El que deberia de funcionar
	def clean(self): 
		if Project.objects.filter(path = self.path).exclude(pk=self.id).exists():
			raise ValidationError({'path':['El path debe de ser unico',]})

	def validate_unique(self, exclude=None):
		#https://docs.djangoproject.com/es/1.9/ref/models/instances/
		if Project.objects.filter(alias = self.alias).exclude(pk=self.id).exists():
			raise ValidationError('El alias ya se encuentra en uso')

	def save(self, force_insert = False, force_update = False):
		self.path = self.alias.replace(" ", "_").lower()
		self.validate_unique()
		super(Project, self).save(force_insert, force_update)

	def get_short_description(self):
		if len(self.description) > 20:
			return self.description[0:20] + "..."
		return self.description
