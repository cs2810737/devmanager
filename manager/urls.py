from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic.base import RedirectView
from rest_framework_jwt.views import obtain_jwt_token

from . import views

app_name = 'manager'
urlpatterns = [
	# url(r'^/$', views.ProjectDetail.as_view()),

	url(r'^projects/$', views.ProjectList.as_view()),
    url(r'^projects/(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view()),
    url(r'^projects/(?P<username>[a-z0-9]+)/$', views.ProjectDetail.as_view()),

    # url(r'^developers/$', views.developer_list),
    url(r'^developers/(?P<user_id>[a-z0-9]+)', views.DeveloperDetail.as_view()),
    url(r'^leads/$', views.Leads.as_view()),

    url(r'^devmembership/$', views.DevMembership.as_view()),
    url(r'^devmembership/(?P<project_id>[0-9])+/$', views.DevMembership.as_view()),
    url(r'^devmembershipdevid/(?P<developer_id>[0-9])+/$', views.DevMembership.as_view()),

    url(r'^users/$', views.Users.as_view()),
    url(r'^users/(?P<id>[a-z0-9]+)$', views.SingleUser.as_view()),

    url(r'^clients/(?P<id>[0-9]+)', views.Clients.as_view()),
    url(r'^clients/$', views.Clients.as_view()),

    url(r'^billables/(?P<id>[0-9]+)', views.Billables.as_view()),
    url(r'^billables/$', views.Billables.as_view()),
    url(r'^devbillables/(?P<dev_id>[0-9]+)/$', views.DevBillableList.as_view()),

    url(r'^payments/(?P<id>[0-9]+)/$', views.Payment.as_view()),
    url(r'^projpayments/(?P<project_id>[0-9]+)/$', views.Payments.as_view()),

    url(r'^accounts/profile/$', RedirectView.as_view(url='<url_to_home_view>', permanent=False), name='index'),
    url(r'^api-token-auth/', obtain_jwt_token),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)