from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^painting/(?P<pk>\d+)/$', views.painting_detail, name='painting_detail'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^index/$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^museums/$', views.museums, name='museums'),
    url(r'^cities/$', views.cities, name='cities'),
    #url(r'^annotate_genres/$', views.annotate_genres, name='annotate_genres'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)