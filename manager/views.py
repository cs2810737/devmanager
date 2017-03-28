from django.shortcuts import render
from django.http import HttpResponse
from models import Project, Billable, Developer

# Create your views here.
def index(request):
	projects = Project.objects.all()
	context = {'projects': projects}
	return render(request, 'manager/index.html', context)

def detail(request, pid):
	billables = Billable.objects.filter(project_id = pid)
	developers = Developer.objects.filter(project_id = pid)
	context = {
		'billables': billables,
		'developers': developers,
	}
	return render(request, 'manager/detail.html', context)