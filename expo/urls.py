from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>\d+)/$', views.painting_detail, name='painting_detail'),
    url(r'^gallery/$', views.gallery ,name='gallery'),
    url(r'^index/$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),

]