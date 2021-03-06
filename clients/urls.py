from django.conf.urls import url
from . import views

app_name = 'client'

urlpatterns = [
    url(r'^create$', views.register, name="register"),
    url(r'^login$', views.login, name="login"),
    url(r'^logout$', views.logout, name="logout"),
		url(r'^show/(?P<username>\w+)/$', views.show, name="show"),
    url(r'^settings$', views.general_settings, name="general_settings"),
    url(r'^settings/image$', views.image_settings, name="image_settings"),
    url(r'^settings/password$', views.change_password, name="change_password"),

    url(r'^delete$', views.delete, name="delete"),
    url(r'^down$', views.down, name="down"),
]