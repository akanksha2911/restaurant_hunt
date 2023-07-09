from django.contrib import admin
from django.urls import path
from rsearch import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path("",views.index,name='rsearch'),
    path("result",views.result,name='result'),
    path("about/<restaurant>/",views.about,name='about')
] 
