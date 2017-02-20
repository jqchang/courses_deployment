from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^submit$', views.submit),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^delete/confirm/(?P<id>\d+)$', views.destroy),
    url(r'^comments/(?P<id>\d+)$', views.comments),
    url(r'^comments/add/(?P<id>\d+)$', views.addComment),
    url(r'^comments/delete/(?P<id>\d+)$', views.deleteComment),
]
