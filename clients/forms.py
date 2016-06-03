# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
#from django.forms import ModelForm
from django import forms
from models import Client


class Login(forms.Form):

	username = forms.CharField(max_length = 20,
		widget=forms.TextInput(attrs={'id': 'username', 'class': 'validate'}))

	password = forms.CharField( max_length = 20,
		widget=forms.PasswordInput(attrs={'id': 'password', 'class': 'validate'}))			


class UserForm(forms.ModelForm):
	password = forms.CharField( widget=forms.PasswordInput(), 
			error_messages = {'required': 'Es necesario ingregar un password' } )
	username = forms.CharField( error_messages = {'required': 'Es necesario ingregar un nombre', 'unique': 'El usuario ya se encuentras registrado',})
	email = forms.CharField( error_messages = {'required': 'Es necesario una dirección de correo'})


	class Meta:
		model = User
		fields = ('username', 'email', 'password')
	
	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({'class' : 'validate'})
		self.fields['email'].widget.attrs.update({'class' : 'validate'})
		self.fields['password'].widget.attrs.update({'class' : 'validate'})
		















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

		
	
