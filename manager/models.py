from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Client(models.Model):
	name = models.CharField(max_length = 50)
	phone_number = models.IntegerField();
	email = models.CharField(max_length = 50);
	address = models.CharField(max_length = 100);

	class Meta:
		ordering = ('name',)

class Developer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	monthly_wage = models.IntegerField(default = 25000)
	# lead = models.BooleanField(default=False)

	class Meta:
		ordering = ('monthly_wage',)

class Lead(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

	# class Meta:
		# ordering = ('user',)

class Project(models.Model):
	name = models.CharField(max_length = 200)
	start_date = models.DateField(default=datetime.date.today)
	lead = models.ForeignKey(User, related_name='projects')
	client = models.ForeignKey(Client, related_name='projects')
	developers = models.ManyToManyField(Developer, through='DevMembership')
	description = models.CharField(max_length = 1000)
	
	class Meta:
		ordering = ('name', )

class Billable(models.Model):
	name = models.CharField(max_length = 50)
	project = models.ForeignKey(Project, related_name = 'billables')
	cost = models.IntegerField(default = 200)
	developer = models.ForeignKey(Developer, related_name='billables')
	recurring = models.BooleanField(default=False)
	reg_date = models.DateField(default=datetime.date.today)
	description = models.CharField(max_length = 300)

	class Meta:
		ordering = ('name',)

class Payment(models.Model):
	billable = models.ForeignKey(Billable, related_name='payments')
	project = models.ForeignKey(Project, related_name='payments')
	date_made = models.DateField(default=datetime.date.today)
	amount = models.IntegerField(default=500)
	comment = models.CharField(max_length = 100)

	class Meta:
		ordering = ('billable_id',)

class DevMembership(models.Model):
	start_date = models.DateField(default=datetime.date.today)
	developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	role = models.CharField(max_length=64)