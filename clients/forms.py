from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
#from django.forms import ModelForm
from django import forms
from models import Client

class UserForm(forms.ModelForm):
	password = forms.CharField( widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'password', 'email')

class UseEditForm(UserChangeForm):
	def __init__(self, *args, **kwargs):
		super(UseEditForm, self).__init__(*args, **kwargs)
		del self.fields['password']

	class Meta:
		model= User
		fields = ('username','first_name', 'last_name')


class ClientForm(forms.ModelForm):
	class Meta:
		model = Client
		fields = ['job', 'bio']

class LoginForm(forms.Form):
	username = forms.CharField(label='username', max_length=50)
	password = forms.CharField(widget=forms.PasswordInput, label="password", max_length=50)
