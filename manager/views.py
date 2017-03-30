from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from manager.models import Project, Billable, Developer
from manager.serializers import ProjectSerializer, BillableSerializer, DeveloperSerializer



@csrf_exempt
def project_list(request):
	if request.method == 'GET':
		projects = Project.objects.all()
		serializer = ProjectSerializer(projects, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = ProjectSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def project_detail(request, pk):
	try:
		project = Project.objects.get(pk=pk)
	except Project.DoesNotExist:
		raise HttpResponse(status=404)

	if request.method == 'GET':
		serializer = ProjectSerializer(project)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = ProjectSerializer(project, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		project.delete()
		return HttpResponse(status=404)

@csrf_exempt
def developer_list(request):
	if request.method == 'GET':
		developers = Developer.objects.all()
		serializer = DeveloperSerializer(developers, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = DeveloperSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def developer_detail(request, pk):
	try:
		developer = Developer.objects.get(pk=pk)
	except Developer.DoesNotExist:
		raise HttpResponse(status=404)

	if request.method == 'GET':
		serializer = DeveloperSerializer(developer)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = DeveloperSerializer(developer, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		developer.delete()
		return HttpResponse(status=404)

@csrf_exempt
def billable_list(request):
	if request.method == 'GET':
		billables = Billable.objects.all()
		serializer = BillableSerializer(billables, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = BillableSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def billable_detail(request, pk):
	try:
		billable = Billable.objects.get(pk=pk)
	except Billable.DoesNotExist:
		raise HttpResponse(status=404)

	if request.method == 'GET':
		serializer = BillableSerializer(billable)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = BillableSerializer(billable, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		billable.delete()
		return HttpResponse(status=404)