from django.conf.urls import url
from . import views

urlpatterns = [
#    url(r'^$', views.root),
    url(r'^users/register$', views.register),
    url(r'^users/login$', views.login),
    url(r'^users/new$', views.new),
    url(r'^users/$', views.index),
]
