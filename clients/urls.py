from django.conf.urls import url
from . import views

app_name = 'client'

urlpatterns = [
    url(r'^/create$', views.register, name="register"),
    url(r'^/login$', views.login_user, name="login"),
]
