from __future__ import unicode_literals

from django.db import models 
from datetime import datetime
from projects.models import Project
from django.contrib.auth.models import User

class Collaborator(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	create_at = models.DateField( default = datetime.now )
	is_admin = models.BooleanField( default = False )
	
	def __str__(self):
		return self.user.username
