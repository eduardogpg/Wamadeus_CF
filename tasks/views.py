from django.shortcuts import render
from .forms import TaskForm

# Create your views here.
def create(request):
	form_task = TaskForm(request.POST or None)
	created = False
	if request.method == 'POST':
		if form_task.is_valid():
			task = form_task(commit = False)
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