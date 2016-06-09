from django.shortcuts import render
from .forms import TaskForm
from django.shortcuts import get_object_or_404
from projects.models import Project
from django.http import HttpResponse
import json

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