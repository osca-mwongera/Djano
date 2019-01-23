from django.urls import re_path

from . import views


app_name = 'land'

urlpatterns = [

    re_path(r'^data/(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.parcel_data, name='landsData'),
    re_path(r'^$', views.parcel_list, name='parcel_list'),
    re_path(r'^(?P<category_slug>[\w-]+)/$', views.parcel_list, name='parcel_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.parcel_detail, name='parcel_detail'),

]
