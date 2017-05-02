from rest_framework import serializers
from manager.models import Client, Project, Developer, Billable
from django.contrib.auth.models import User

class BillableSerializer(serializers.ModelSerializer):

	class Meta:
		model = Billable
		fields = ('id', 'name', 'project', 'cost', 'developer', 'recurring', 'reg_date', 'description' )

class DeveloperSerializer(serializers.ModelSerializer):
	billables = BillableSerializer(many=True)

	class Meta:
		model = Developer
		fields = ('name', 'monthly_wage', 'billables')

class ProjectSerializer(serializers.ModelSerializer):
	developers = DeveloperSerializer(many=True)
	billables = BillableSerializer(many=True)

	class Meta:
		model = Project
		fields = ('name', 'start_date', 'client', 'developers', 'billables', 'description')

class ClientSerializer(serializers.ModelSerializer):
	projects = ProjectSerializer(many=True)

	class Meta:
		model = Client
		fields = ('name', 'projects')
