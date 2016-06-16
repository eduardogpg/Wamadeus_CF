from django.contrib import admin
from .models import Status
from .models import Project
# Register your models here.

admin.site.register(Project)
admin.site.register(Status)

