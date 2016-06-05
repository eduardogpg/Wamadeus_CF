from django import forms
from .models import Status, Project

class ProjectForm(forms.ModelForm):
	
	dead_line = forms.DateField( widget = forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',))

	class Meta:	
		model = Project
		exclude = ['create_at', 'user', 'path']

	def __init__(self, *args, **kwargs):
		super(ProjectForm, self).__init__(*args, **kwargs)
		self.fields['name'].widget.attrs.update({'class' : 'validate'})
		self.fields['alias'].widget.attrs.update({'class' : 'validate'})
		self.fields['description'].widget.attrs.update({'class' : 'materialize-textarea'})
		self.fields['status'].widget.attrs.update({})
		self.fields['dead_line'].widget.attrs.update({'class' : 'datepicker_'})

	def clean_alias(self):
		return
		alias = self.cleaned_data['alias']
		if alias == "ismael":
			#raise ValidationError('Too many characters ...')
			alias = "Control"
		return alias

	def clean_alias(self):
		alias = self.cleaned_data['alias']
		if Project.objects.filter(alias = alias).exists():
				#raise forms.ValidationError("")
			 raise forms.ValidationError("El alias ya se encuentra en uso")
		return alias


class StatusForm(forms.ModelForm):
	class Meta:
		model = Status
		fields = '__all__'
