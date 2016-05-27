from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Client(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.CharField(max_length = 50)
	job = models.CharField(max_length = 20)


	def __str__(self):
		return self.user.username