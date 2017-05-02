from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from manager.models import Project, Billable, Developer
from manager.serializers import ProjectSerializer, BillableSerializer, DeveloperSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib.auth.models import User
from rest_framework import permissions, status

class ProjectList(APIView):
	def get_object(self, username):
		try:
			return Project.objects.filter(usernames_in=username)
		except Project.DoesNotExist:
			raise Http404

	def get(self, request, format=None):
		projects = Project.objects.all()
		serializer = ProjectSerializer(projects, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = ProjectSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProjectDetail(APIView):
	def get_object(self, pk):
		try:
			return Project.objects.get(pk=pk)
		except Project.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		project = self.get_object(pk)
		serializer = ProjectSerializer(project)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		project = self.get_object(pk)
		serializer = ProjectSerializer(project, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		project = self.get_object(pk)
		project.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



class Billables(APIView):
	def get_object(self, id):
		try:
			return Billable.objects.get(id=id)
		except Billable.DoesNotExist:
			raise Http404

	def get(self, request, format=None):
		projects = Billable.objects.all()
		serializer = BillableSerializer(projects, many=True)
		return Response(serializer.data)

	def put(self, request, id, format=None):
		billable = self.get_object(id)
		serializer = BillableSerializer(billable, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def post(self, request, format=None):
		serializer = BillableSerializer(data=request.data)
		if serializer.is_valid():
			# print request.data
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, id, format=None):
		billable = self.get_object(id)
		billable.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class DevBillableList(APIView):
	def get_object(self, dev_id):
		try:
			return Billable.objects.filter(developer_id=dev_id)
		except Billable.DoesNotExist:
			raise Http404

	def get(self, request, dev_id, format=None):
		billables = self.get_object(dev_id)
		serializer = BillableSerializer(billables, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = BillableSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def perform_create(self, serializer):
		serializer.save(developer=self.request.user)

	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class SingleBillable(APIView):
	def get_object(self, id):
		try:
			return Billable.objects.get(id=id)
		except Billable.DoesNotExist:
			raise Http404

	def get(self, request, id):
		billable = self.get_object(id)
		serializer = DeveloperSerializer(billable)
		return Response(serializer.data)



class DeveloperDetail(APIView):
	def get_object(self, username):
		try:
			return Developer.objects.get(name=username)
		except Developer.DoesNotExist:
			raise Http404

	def get(self, request, username):
		developer = self.get_object(username)
		serializer = DeveloperSerializer(developer)
		return Response(serializer.data)