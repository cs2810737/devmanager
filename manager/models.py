from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
class Client(models.Model):
	name = models.CharField(max_length = 50)

	class Meta:
		ordering = ('name',)

class Developer(models.Model):
	name = models.CharField(max_length = 50)
	monthly_wage = models.IntegerField(default = 25000)

	class Meta:
		ordering = ('name',)

class Project(models.Model):
	name = models.CharField(max_length = 200)
	start_date = models.DateField(default=datetime.date.today)
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

class DevMembership(models.Model):
	developer = models.ForeignKey(Developer)
	project = models.ForeignKey(Project)

# class ProjectOwnership(models.Model):
# 	project = models.ForeignKey(Project)
# 	client = models.ForeignKey(Client)