from rest_framework import serializers
from manager.models import Project, Developer, Billable

class DeveloperSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Developer
		fields = ('name','hourly_rate','project', 'hours_worked', )

class BillableSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Billable
		fields = ('name', 'project', 'cost' )

class ProjectSerializer(serializers.ModelSerializer):
	developers = DeveloperSerializer(many=True)
	billables = BillableSerializer(many=True)

	class Meta:
		model = Project
		fields = ('name', 'developers','billables')
