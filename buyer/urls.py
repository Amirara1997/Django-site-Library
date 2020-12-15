from django.urls import path,include
from . import views2

urlpatterns =  [
    path('creater', views2.creater, name='creater'),
    path('home2', views2.home2, name='home2'),
    path('home3', views2.home3, name='home3'),
    path('home4', views2.home4, name='home4'),

]