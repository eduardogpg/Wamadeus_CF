from django.conf.urls import url
from . import views

app_name = 'client'

urlpatterns = [
    url(r'^create$', views.register, name="register"),
    url(r'^login$', views.login, name="login"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^settings$', views.settings, name="settings"),
    url(r'^delete$', views.delete, name="delete"),
    url(r'^down$', views.down, name="down"),
]
