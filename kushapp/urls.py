from django.conf.urls import url

from . import views

#This block is needed to map our urls to views. Parameter "name" allows to use simple alias in view or on html.
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<author_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<author_id>[0-9]+)/books/$', views.books, name='books'),
	url(r'^(?P<author_id>[0-9]+)/update/$', views.update, name='update'),
]
