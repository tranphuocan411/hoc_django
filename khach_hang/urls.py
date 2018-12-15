from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from khach_hang import views

app_name = 'khach_hang'

urlpatterns = [
    url(r'^dang_nhap/$', views.dang_nhap, name='dang_nhap'),
    url(r'^quan_tri/$', views.quan_tri, name='quan_tri'),
    url(r'^dang_xuat/$', views.dang_xuat, name='dang_xuat'),
    url(r'^dang_ky/$', views.dang_ky, name='dang_ky'),
]