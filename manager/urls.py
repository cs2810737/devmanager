from django.conf.urls import url
from django.views.generic.base import RedirectView

from . import views

app_name = 'manager'
urlpatterns = [
	url(r'^(?P<pk>[0-9]+)/$', views.project_detail),
	url(r'^projects/$', views.project_list),
    url(r'^projects/(?P<pk>[0-9]+)/$', views.project_detail),
    url(r'^developers/$', views.developer_list),
    url(r'^developers/(?P<pk>[0-9]+)/$', views.developer_detail),
    url(r'^billables/$', views.billable_list),
    url(r'^billables/(?P<pk>[0-9]+)/$', views.billable_detail)
]