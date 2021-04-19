# -*- coding: utf-8 -*-
from django.urls import path
from .import views

urlpatterns=[
   
    path('docregister',views.docregister,name='docregister'),
    path('doclogin',views.doclogin,name='doclogin'),
    path('doclogin/heart',views.heart,name='heart'),
    path('doclogin/bcancer',views.bcancer,name='bcancer'),
    path('doclogin/dia',views.dia,name='dia'),
    
    ]
