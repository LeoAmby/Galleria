from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$', views.home, name = 'home'),
    url(r'^travel$', views.travel, name='travel'),
    url(r'^cuisine$', views.cuisine, name='cuisine'),
    url(r'^family$', views.family, name='family'),
    url(r'^search/', views.search_results, name='search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)