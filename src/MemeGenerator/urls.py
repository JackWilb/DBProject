from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('makeameme/', views.makeameme, name='makeameme'),
    path('makeatag/', views.makeatag, name='makeatag'),
    path('makeanaccount/', views.makeanaccount, name='makeanaccount')
]
