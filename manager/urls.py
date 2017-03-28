from django.conf.urls import url
from django.views.generic.base import RedirectView

from . import views

app_name = 'manager'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<pid>[0-9]+)/$', views.detail, name='detail'),
]