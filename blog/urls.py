from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='blog/home'),
    path('strings/',views.strings,name='blog/strings'),
    path('list/', views.list, name='blog/list'),
    path('D_ORM/', views.D_ORM, name='blog/D_ORM'),
    path('GIT/', views.GIT, name='blog/GIT'),
    path('Functions/', views.Functions, name='blog/Functions'),
    path('Functions2/', views.Functions2, name='blog/Functions2'),

    path('Avro/', views.Avro, name='blog/Avro'),
    path('Web_Scrapping/', views.Web_Scrapping, name='blog/Web_Scrapping'),
    path('Host_Project_in_pythonAnywhere/', views.Host_Project_in_pythonAnywhere, name='blog/Host_Project_in_pythonAnywhere'),
    path('github/', views.github, name='blog/github'),


]
