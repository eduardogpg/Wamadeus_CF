from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from models import Client
from forms import UserForm, Login, ClientForm , UseEditForm

from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from django.shortcuts import get_object_or_404
# Create your views here.
#Tutorial to register new User
#http://www.tangowithdjango.com/book/chapters/login.html

def register(request):
	registered = False
	form = UserForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			user = form.save()
			user.set_password(user.password)
			user.save()
			registered = True
		else:
			print form.errors
	else:
		form = UserForm()
	context = {'form' : form, 'registered' : registered}
	return render(request, 'register.html', context )

def user_is_not_login(user):
    return not user.is_authenticated()

@user_passes_test(user_is_not_login, login_url='dashboard')
def login(request):
	message = None
	if request.method == 'POST':
		user = authenticate(username = request.POST['username'], password = request.POST['password'])
		if user is not None:
			if user.is_active:
				login_django(request, user)
				return redirect('dashboard')
			else:
				message = "El usuar esta desabilitado"
		else:
			message = "El usuario o la password son incorrectos"
	
	form = Login()
	context = { 'form' : form, 'message' : message }
	return render(request, 'login.html',  context ) 

@login_required(login_url='home')
def settings(request):
	updated = False

	client_form = create_form_client( request )
	user_form = UseEditForm(request.POST or None, instance = request.user)

	if request.method == 'POST':
		if user_form.is_valid() and client_form.is_valid():
			client = client_form.save(commit=False)
			user = user_form.save(commit = False)
			client.user = user
			user.save()
			client.save()
			updated = True

	context = { 'client_form': client_form, 'user_form' : user_form, 'updated': updated}
	return render(request, 'settings.html', context)

@login_required(login_url='home')
def delete(request):
	user = request.user
	user.delete()
	return redirect('home')

@login_required(login_url='home')
def down(request):
	user = request.user
	user.is_active = False
	user.save()
	return redirect('client:logout')

def logout(request):
	logout_django(request)
	return redirect('home')

def create_form_client(request):
	try:
		return ClientForm(request.POST or None, instance = request.user.client)
	except:
		return ClientForm(request.POST or None)	

		




