from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Project(models.Model):
	name = models.CharField(max_length = 200)
	def __unicode__(self):
		return 'Project: ' + self.name

class Developer(models.Model):
	name = models.CharField(max_length = 50)
	hourly_rate = models.IntegerField(default = 250)
	project = models.ForeignKey(Project)
	hours_worked = models.IntegerField(default = 0)
	def __unicode__(self):
		return 'Developer: ' + self.name

class Billable(models.Model):
	name = models.CharField(max_length = 50)
	project = models.ForeignKey(Project)
	cost = models.IntegerField(default = 200)
	def __unicode__(self):
		return 'Billable: ' + self.name