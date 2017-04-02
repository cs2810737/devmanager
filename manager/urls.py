from django.conf.urls import url
from django.views.generic.base import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'manager'
urlpatterns = [
	url(r'^(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view()),
	url(r'^projects/$', views.ProjectList.as_view()),
    url(r'^projects/(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view()),
    # url(r'^projects/(?P<pk>[0-9]+)/$', views.project_detail),
    # url(r'^developers/$', views.developer_list),
    # url(r'^developers/(?P<pk>[0-9]+)/$', views.developer_detail),
    # url(r'^billables/$', views.billable_list),
    # url(r'^billables/(?P<pk>[0-9]+)/$', views.billable_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)