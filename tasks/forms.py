from django import forms
from .models import Task
from django.contrib.auth.models import User
from contributors.models import Collaborator


class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		exclude = ['create_at', 'project']
	
	def __init__(self, *args, **kwargs):
		project_id = kwargs.pop('project_id', None)#es necesario sacar este valor
		super(TaskForm, self).__init__(*args, **kwargs)

		self.fields['title'].widget.attrs.update({'class' : 'validate'})
		self.fields['description'].widget.attrs.update({'class' : 'materialize-textarea'})
		self.fields['status'].widget.attrs.update({'class': ''})
		self.fields['assigned_to'].widget.attrs.update({'class': ''})
		self.fields['dead_line'].widget.attrs.update({'class' : 'datepicker'})
		
		#self.fields['assigned_to'].queryset = User.objects.filter( is_superuser = True)
		self.fields['assigned_to'].queryset = Collaborator.objects.filter( project_id = project_id)

	def get_colaboradores(self, project_id):
		colaboradores = Collaborator.objects.filter( project_id = project_id )
		
	