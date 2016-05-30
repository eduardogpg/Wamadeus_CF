from django.shortcuts import render

# Create your views here.
def create(request):
	return render(request, 'tasks/create.html', {} )

def show(request, task_id = None):
	return render(request, 'tasks/show.html', {} )

def index(request, project_id = None):
	return render(request, 'tasks/index.html', {} )

def edit(request, task_id = None):
	return render(request, 'tasks/edit.html', {} )