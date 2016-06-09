from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from models import Client
from forms import UserForm, Login, ClientForm , UseEditForm, ClientImageForm

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
	message = None
	form = UserForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			user = form.save(commit = False)
			password = user.password
			user.set_password(password)
			user.save()
			Client(user = user).save()
			user_authenticated = authenticate(username = user.username, password = password)
			login_django(request, user_authenticated)
			return redirect('dashboard')
		else:
			message = form.errors.as_data().itervalues().next()[0].message
	context = {'form' : form, 'message' : message}
	return render(request, 'clients/register.html', context )

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
				message = "El usuario esta deshabilitado"
		else:
			message = "El usuario o la password son incorrectos"
	
	form = Login()
	context = { 'form' : form, 'message' : message }
	return render(request, 'clients/login.html',  context ) 

@login_required(login_url='home')
def general_settings(request):
	message = None
	client_form = create_form_client( request )
	user_form = UseEditForm(request.POST or None, instance = request.user)
	if request.method == 'POST':
		if user_form.is_valid() and client_form.is_valid():
			client = client_form.save(commit=False)
			user = user_form.save(commit = False)
			client.user = user
			user.save()
			client.save()
			message = "Perfil actualizado"
		else:
			message = "El formulario contiene errores"

	context = { 'client_form': client_form, 'user_form' : user_form, 'message': message}
	return render(request, 'clients/settings.html', context)


@login_required(login_url='home')
def image_settings(request):
	message = None
	user = get_object_or_404(Client, user_id= request.user.id)

	form = ClientImageForm(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if form.is_valid():
			user.image = form.cleaned_data['image']
			user.save()
			message = "Se actualizado la imagen de perfil"

	context = { 'form': form, 'user': user ,'message': message}
	return render(request, 'clients/settings_image.html', context)


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

def show(request, username = None):
	user = get_object_or_404(User, username = username)
	context = {'user' : user}
	return render(request, 'clients/show.html', context)
	
def logout(request):
	logout_django(request)
	return redirect('home')

def create_form_client(request):
	try:
		return ClientForm(request.POST or None, instance = request.user.client)
	except:
		return ClientForm(request.POST or None)	







