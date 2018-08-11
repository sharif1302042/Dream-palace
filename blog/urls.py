from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='blog/home'),
    path('post_details/',views.post_details,name='blog/post_details'),
    path('post_details2/', views.post_details2, name='blog/post_details2'),
    path('post_details3/', views.post_details3, name='blog/post_details3'),
    path('post_details4/', views.post_details4, name='blog/post_details4'),
    path('post_details5/', views.post_details5, name='blog/post_details5'),
    path('post_details6/', views.post_details6, name='blog/post_details6'),
    path('post_details7/', views.post_details7, name='blog/post_details7'),


]
