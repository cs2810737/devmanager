from django.conf.urls import url
from django.views.generic.base import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic.base import RedirectView

from . import views

app_name = 'manager'
urlpatterns = [
	# url(r'^/$', views.ProjectDetail.as_view()),

	url(r'^projects/$', views.ProjectList.as_view()),
    url(r'^projects/(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view()),

    # url(r'^developers/$', views.developer_list),
    url(r'^developers/(?P<username>[a-z0-9]+)', views.DeveloperDetail.as_view()),

    url(r'^billables/(?P<id>[0-9]+)', views.Billables.as_view()),
    url(r'^billables/$', views.Billables.as_view()),
    url(r'^devbillables/(?P<dev_id>[0-9]+)/$', views.DevBillableList.as_view()),

    url(r'^accounts/profile/$', RedirectView.as_view(url='<url_to_home_view>', permanent=False), name='index')
]

urlpatterns = format_suffix_patterns(urlpatterns)