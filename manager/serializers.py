from rest_framework import serializers
from manager.models import Client, Project, Developer, Billable, DevMembership, Lead, Payment
from django.contrib.auth.models import User

class BillableSerializer(serializers.ModelSerializer):

	class Meta:
		model = Billable
		fields = ('id', 'name', 'project', 'cost', 'developer', 'recurring', 'reg_date', 'description' )

class PaymentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Payment
		fields = ('id', 'date_made', 'amount', 'comment', 'billable', 'project')

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('id', 'username', )

class LeadSerializer(serializers.ModelSerializer):

	class Meta:
		model = Lead
		fields = ('user',)

class DeveloperSerializer(serializers.ModelSerializer):
	user = UserSerializer()

	class Meta:
		model = Developer
		fields = ( 'user', 'monthly_wage', )

class ProjectSerializer(serializers.ModelSerializer):
	developers = DeveloperSerializer(many=True, read_only=True)
	billables = BillableSerializer(many=True, read_only=True)
	payments = PaymentSerializer(many=True, read_only=True)

	class Meta:
		model = Project
		fields = ('id', 'name', 'start_date', 'lead', 'developers', 'billables', 'payments', 'description', 'client')

class ClientSerializer(serializers.ModelSerializer):

	class Meta:
		model = Client
		fields = ('id', 'name', 'phone_number', 'email', 'address')

class DevMembershipSerializer(serializers.ModelSerializer):

	class Meta:
		model = DevMembership
		fields = ('id', 'developer', 'start_date', 'role', 'project' )


