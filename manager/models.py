from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Project(models.Model):
	name = models.CharField(max_length = 200)
	
	class Meta:
		ordering = ('name', )

class Developer(models.Model):
	name = models.CharField(max_length = 50)
	hourly_rate = models.IntegerField(default = 250)
	project = models.ForeignKey(Project, related_name='developers')
	hours_worked = models.IntegerField(default = 0)

	class Meta:
		ordering = ('name',)

class Billable(models.Model):
	name = models.CharField(max_length = 50)
	project = models.ForeignKey(Project, related_name = 'billables')
	cost = models.IntegerField(default = 200)

	class Meta:
		ordering = ('name',)
