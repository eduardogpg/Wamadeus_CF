from django import forms
from .models import Status, Project

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		exclude = ['create_at', 'user', 'path']
		
class StatusForm(forms.ModelForm):
	class Meta:
		model = Status
		fields = '__all__'