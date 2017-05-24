from rest_framework import serializers
from manager.models import Client, Project, Developer, Billable, Lead
from django.contrib.auth.models import User

class BillableSerializer(serializers.ModelSerializer):

	class Meta:
		model = Billable
		fields = ('id', 'name', 'project', 'cost', 'developer', 'recurring', 'reg_date', 'description' )

class DeveloperSerializer(serializers.ModelSerializer):
	# billables = BillableSerializer(many=True)

	class Meta:
		model = Developer
		fields = ('user_id', 'monthly_wage', )

# class UserSerializer(serializers.ModelSerializer):
# 	developer = DeveloperSerializer()

# 	class Meta:
# 		model = User
# 		fields = ('id', 'username', 'developer')

class ProjectSerializer(serializers.ModelSerializer):
	developers = DeveloperSerializer(many=True)
	# developers = UserSerializer(many=True)
	billables = BillableSerializer(many=True)

	class Meta:
		model = Project
		fields = ('id', 'name', 'start_date', 'lead', 'client', 'developers', 'billables', 'description', 'lead')

class ClientSerializer(serializers.ModelSerializer):
	# projects = ProjectSerializer(many=True, read_only=True)

	class Meta:
		model = Client
		fields = ('id', 'name', 'phone_number', 'email', 'address')

class LeadSerializer(serializers.ModelSerializer):
	# user = 

	class Meta:
		model = Lead
		fields = ('user_id', )

class UserSerializer(serializers.ModelSerializer):
	# user = 

	class Meta:
		model = User
		fields = ('id', 'username')
