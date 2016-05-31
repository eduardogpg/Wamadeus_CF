from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import ProjectForm, StatusForm
from .models import Status, Project

@login_required(login_url='home')
def create(request):
	created = False
	form_project =  ProjectForm(request.POST or None)

	if request.method == 'POST':
		if form_project.is_valid():
			project = form_project.save(commit = False)
			project.user = request.user
			project.save()
			created = True

	context = { 'form_project': form_project, 'created': created}
	return render(request, 'create.html', context)

def show(request, project_id = None):
	project = get_object_or_404(Project, id= project_id)
	is_admin = is_project_admin(request, project.user_id)
	context = { 'project': project, 'is_admin': is_admin}
	return render(request, 'show.html', context)

def index(request, user_id):
	projects = Project.objects.all().filter(user_id = user_id)
	context = { 'user': request.user, 'projects': projects }
	return render( request, 'index.html', context)

def edit(request, project_id):
	project = get_object_or_404(Project, id=project_id)
	updated = False
	form_project = ProjectForm(request.POST or None, instance = project)

	if request.method == 'POST':
		if form_project.is_valid():
			form_project.save()
			updated = True

	context =  { 'form_project' : form_project , 'updated': updated, 'project': project}
	return render(request, 'edit.html', context)


def create_status(request):
	status_form = StatusForm(request.POST or None)
	created = False
	if request.method == 'POST':
		if status_form.is_valid():
			status_form.save()
			created = True

	context = {'status_form': status_form, 'created': created} 
	return render(request, 'status/create.html', context)

def show_status(request, status_id = None):
	status = get_object_or_404(Status, pk=status_id)
	context = { 'status' : status }
	return render(request, 'status/show.html', context)	

def update_status(request, status_id= None):
	status = get_object_or_404(Status, pk=status_id)
	updated = False
	status_form = StatusForm(request.POST or None, instance = status)
	if request.method == 'POST':
		if status_form.is_valid():
			status_form.save()
			updated = True

	context = {'updated': updated, 'status_form': status_form}
	return render(request, 'status/edit.html', context )

def show_path(request, path):
	project = get_object_or_404(Project, path = path)
	is_admin = is_project_admin(request, project.user_id)
	context = { 'project': project, 'is_admin': is_admin}
	return render(request, 'show.html', context)


def is_project_admin(request, user_id):
	if request.user is None or user_id != request.user.id:
		return False
	return True
	





