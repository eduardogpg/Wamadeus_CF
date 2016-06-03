from django.conf.urls import url
from . import views
app_name = 'task'

urlpatterns = [
		url(r'^create/(?P<project_id>[0-9]+)/$', views.create, name="create"),
		url(r'^show/(?P<task_id>[0-9]+)/$', views.show, name="show"),
		url(r'^index/(?P<project_id>[0-9]+)/$', views.index, name="index"),
		url(r'^edit/(?P<task_id>[0-9]+)/$', views.edit, name="edit"),
]