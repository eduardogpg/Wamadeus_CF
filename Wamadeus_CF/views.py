from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from projects.models import Project

def home(request):
	if request.user.is_authenticated():
		return redirect("dashboard")
	else:
		last_projects = Project.objects.all()[:10]
		context = { 'last_projects': last_projects }
		return render(request, 'wamadeus/home.html', context)

@login_required(login_url='home')
def dashboard(request):
	context = { 'user': request.user}
	return render(request, 'clients/dashboard.html', context)	