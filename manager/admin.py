from django.contrib import admin
from .models import Client, Project, Developer, Billable

# Register your models here.
admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Developer)
admin.site.register(Billable)