from django.conf.urls import url
from . import views

# pull the local views.py file from local dir

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<id>[0-9]+)$', views.detail, name = 'detail'),
]

