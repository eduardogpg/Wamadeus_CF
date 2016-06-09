from .forms import TaskForm
from django.shortcuts import get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json
from .models import Task
from django.shortcuts import render, redirect

# Create your views here.
def create_task(request):
	print "Entro"
	if request.method == 'POST':
		form = TaskForm(request.POST)
		response_data = {}
		if form.is_valid():
			task = form.save(commit = False)
			task.project_id = 12	
			response_data['status'] = '200'
			response_data['title'] = task.title
			response_data['description'] = task.description
			response_data['color'] = task.status.color
			response_data['dead_line'] = str(task.dead_line)
			task.save()
		else:
			response_data['error'] = form.errors.as_data().itervalues().next()[0].message
		
		return HttpResponse(
			json.dumps(response_data),
			content_type="application/json"
		)
	else:
		return HttpResponse(
			json.dumps({"nothing to see": "just post method"}),
				content_type="application/json"
			)

@login_required(login_url='home')
def create(request, path = None):
	project  = get_object_or_404( Project, path= path )
	form = TaskForm(request.POST or None, project_id = project.id)
	message = None
	if request.method == 'POST':
		if form.is_valid():
			task = form.save(commit = False)
			task.project = project
			task.save()
			return redirect('task:show', task_id = task.id)
		else:
			message = "Tarea no creada"
	context = { 'form': form, 'message': message}
	return render(request, 'tasks/create.html', context )

def show(request, task_id = None):
	task = get_object_or_404( Task, id = task_id )
	form = TaskForm(request.POST or None, instance = task)
	context = {'form' : form, 'task': task}
	return render(request, 'tasks/show.html', context )



def index(request, project_id = None):
	return render(request, 'tasks/index.html', {} )

def edit(request, task_id = None):
	return render(request, 'tasks/edit.html', {} )