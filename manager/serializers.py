from rest_framework import serializers
from manager.models import Project, Developer, Billable

class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = ('name',)

class DeveloperSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Developer
		fields = ('hourly_rate','project', 'hours_worked', )

class BillableSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Billable
		fields = ('name', 'project', 'cost' )
