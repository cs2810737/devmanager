from rest_framework import serializers
from manager.models import Project, Developer, Billable
from django.contrib.auth.models import User


class BillableSerializer(serializers.ModelSerializer):

	class Meta:
		model = Billable
		fields = ('id','name', 'project', 'cost', 'developer' )

class DeveloperSerializer(serializers.ModelSerializer):
	billables = BillableSerializer(many=True)

	class Meta:
		model = Developer
		fields = ('name','hourly_rate','project', 'hours_worked', 'billables')

class ProjectSerializer(serializers.ModelSerializer):
	developers = DeveloperSerializer(many=True)
	billables = BillableSerializer(many=True)

	class Meta:
		model = Project
		fields = ('name', 'developers','billables',)
