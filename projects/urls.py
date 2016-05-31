from django.conf.urls import url
from . import views

app_name = 'project'
urlpatterns = [
		url(r'^create$', views.create, name="create"),
		url(r'^show/(?P<project_id>[0-9]+)/$', views.show, name="show"),
		url(r'^show/(?P<path>\w+)/$', views.show_path, name="show_path"),
		url(r'^index/(?P<user_id>[0-9]+)/$', views.index, name="index"),
		url(r'^edit/(?P<project_id>[0-9]+)/$', views.edit, name="edit"),
		url(r'^status/create$', views.create_status, name="create_status"),
		url(r'^status/show/(?P<status_id>[0-9]+)/$', views.show_status, name="show_status"),
		url(r'^status/update/(?P<status_id>[0-9]+)/$', views.update_status, name="update_status"),
]