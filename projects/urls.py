from django.conf.urls import url
from . import views

app_name = 'project'
urlpatterns = [
		url(r'^create$', views.create, name="create"),
		url(r'^status/create$', views.create_status, name="create_status"),
		url(r'^status/show/(?P<status_id>[0-9]+)/$', views.show_status, name="show_status"),
		url(r'^status/update/(?P<status_id>[0-9]+)/$', views.update_status, name="update_status"),
]