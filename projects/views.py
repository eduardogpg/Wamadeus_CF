from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import ProjectForm, StatusForm
from .models import Status


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









