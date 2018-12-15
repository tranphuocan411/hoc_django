from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from first_app import views

app_name = 'first_app'

urlpatterns = [
    url(r'^tao/$', views.tao_cookie, name='tao_cookie'),
    url(r'^register/$',views.register,name='register'),
]