# -*- coding: utf-8 -*-
from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('patregister',views.patregister,name='patregister'),
    path('patlogin',views.patlogin,name='patlogin'),
    path('news',views.news,name='news')
    
    ]
