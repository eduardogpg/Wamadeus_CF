from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from projects.models import Status, Project

# Create your models here.
class Task(models.Model):
	title = models.CharField(max_length = 50)
	description = models.TextField(max_length= 200)
	status = models.ForeignKey(Status)
	project = models.ForeignKey(Project)
	create_at = models.DateField( default = datetime.now )
	dead_line = models.DateField()

	def __str__(self):
		return self.title