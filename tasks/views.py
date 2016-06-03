from django.shortcuts import render
from .forms import TaskForm
from django.shortcuts import get_object_or_404
from projects.models import Project

# Create your views here.
def create(request, project_id = None):
	form_task = TaskForm(request.POST or None)
	project  = get_object_or_404( Project, id= project_id )
	created = False
	if request.method == 'POST':
		if form_task.is_valid():
			task = form_task.save(commit = False)
			task.project = project
			task.save()
			created = True

	context = { 'form_task': form_task, 'created': created}
	return render(request, 'tasks/create.html', context )

def show(request, task_id = None):
	return render(request, 'tasks/show.html', {} )

def index(request, project_id = None):
	return render(request, 'tasks/index.html', {} )

def edit(request, task_id = None):
	return render(request, 'tasks/edit.html', {} )