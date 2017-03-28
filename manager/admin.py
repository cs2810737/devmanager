from django.contrib import admin
from .models import Project, Developer, Billable

# Register your models here.
admin.site.register(Project)
admin.site.register(Developer)
admin.site.register(Billable)