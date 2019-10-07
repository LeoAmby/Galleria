from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$', views.home, name = 'home'),
    url(r'^travel/$', views.travel,),
    url(r'^cuisine/$', views.cuisine),
    url(r'^family/$', views.family),
    url(r'^search/', views.search_results, name='search_results')
]