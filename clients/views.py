from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from forms import UserForm, LoginForm

from django.contrib.auth import authenticate, login

# Create your views here.
#Tutorial to register new User
#http://www.tangowithdjango.com/book/chapters/login.html
def home(request):
	return render(request, 'home.html', {})

def dashboard(request):
	return render(request, 'dashboard.html', {})	

def login_user(request):
	message = None
	if request.method == 'POST':
		user = authenticate(username = request.POST['username'], password= request.POST['password'])
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('dashboard')
			else:
				message = "The password id valid, but the account has been disbled"
		else:
			message = "The username and password were incorrect"
	
	login_form = LoginForm()
	context = { 'login_form' : login_form, 'message' : message }
	return render(request, 'login.html',  context ) 

def register(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered = True
			print "new user register"
		else:
			print user_form.errors
	else:
		user_form = UserForm()

	context = {'user_form' : user_form, 'registered' : registered}
	return render(request, 'register.html', context )
