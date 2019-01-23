from django.urls import re_path

from . import views

app_name = 'houses'

urlpatterns = [

    re_path(r'^data/(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.house_data, name='houseData'),
    re_path(r'^$', views.house_list, name='house_list'),
    re_path(r'^(?P<category_slug>[\w-]+)/$', views.house_list, name='house_list_by_type'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.house_detail, name='house_detail'),

]