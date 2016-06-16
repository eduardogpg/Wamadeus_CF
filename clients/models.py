from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

def upload_location(instance, filename):
	filebase, extension = filename.split(".")
	return "image_profile/%s/%s.%s" % (instance.id, instance.id, extension)

class Client(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length = 200)
	job = models.CharField(max_length = 50)
	#image = models.FileField( upload_to="user/profile/", null = True, blank=True )
	#pip install Pillow
	#image = models.ImageField( upload_to="user/profile/", null = True, blank=True )
	image = models.ImageField( upload_to=upload_location, null = True, blank=True )

	def __str__(self):
		return self.user.username