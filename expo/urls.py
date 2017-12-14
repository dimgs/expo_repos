from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.painting_list, name='painting_list'),
]