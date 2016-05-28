from django.shortcuts import render
from .forms import ProjectForm

def create(request):
	form_project =  ProjectForm(request.POST or None)
	context = { 'form_project': form_project}
	return render(request, 'create.html', context)
