from django import forms
from .models import Status, Project

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		exclude = ['dead_line']
		