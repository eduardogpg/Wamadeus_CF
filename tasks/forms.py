from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		exclude = ['create_at', 'project']
	
	def __init__(self, *args, **kwargs):
		super(TaskForm, self).__init__(*args, **kwargs)
		self.fields['title'].widget.attrs.update({'class' : 'validate'})
		self.fields['description'].widget.attrs.update({'class' : 'materialize-textarea'})
		self.fields['status'].widget.attrs.update({'class': ''})
		self.fields['dead_line'].widget.attrs.update({'class' : 'datepicker'})
	
