from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
from forms import UserForm


# Create your views here.
#Tutorial to register new User
#http://www.tangowithdjango.com/book/chapters/login.html
def dashboard(request):
	return HttpResponse("Hola mundo")

def create_user(request):
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

	context = {'user_form' : user_form, 'registered' : True}
	return render(request, 'register.html', context )
