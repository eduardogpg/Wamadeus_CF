from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Client(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length = 200)
	job = models.CharField(max_length = 50)
	image = models.FileField( upload_to="user/profile/", null = True, blank=True )

	def __str__(self):
		return self.user.username