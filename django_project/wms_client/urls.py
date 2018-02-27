# coding=utf-8
"""URI Routing configuration for this apps."""
from django.conf.urls import url
from . import views

app_name = 'wms_client'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^map/(?P<slug>[\w-]+)/$', views.map, name='map'),
]
