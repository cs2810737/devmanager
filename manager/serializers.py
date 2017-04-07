from rest_framework import serializers
from manager.models import Project, Developer, Billable
from django.contrib.auth.models import User


class BillableSerializer(serializers.ModelSerializer):
	# name = serializers.CharField(max_length = 50)
	# project = serializers.RelatedField(read_only=True)
	# cost = serializers.IntegerField(default = 200)
	# developer = serializers.RelatedField(read_only=True)

	# def create(self, validated_data):
	# 	return Billable(**validated_data)

	class Meta:
		model = Billable
		fields = ('name', 'project', 'cost', 'developer' )

class DeveloperSerializer(serializers.ModelSerializer):
	billables = BillableSerializer(many=True)

	class Meta:
		model = Developer
		fields = ('name','hourly_rate','projects', 'hours_worked', 'billables',)

class ProjectSerializer(serializers.ModelSerializer):
	developers = DeveloperSerializer(many=True)
	billables = BillableSerializer(many=True)

	class Meta:
		model = Project
		fields = ('name', 'developers','billables',)
