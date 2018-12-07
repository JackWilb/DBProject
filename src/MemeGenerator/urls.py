from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import 
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('makeameme/', views.makeameme, name='makeameme')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
