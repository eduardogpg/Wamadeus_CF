from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^/$', views.dashboard, name="user"),
    url(r'^/create$', views.create_user, name="create_user"),
]
