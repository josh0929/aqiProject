from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^', views.Home, name='Home'),
    url(r'^about/', views.About, name='About'),
]
