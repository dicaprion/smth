from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^dron/$', views.index, name='index'),
]