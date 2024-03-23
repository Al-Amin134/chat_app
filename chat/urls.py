from django.urls import path
from . import views

urlpatterns = [
    path('weather/',views.weather, name= 'weather'),
     path('', views.home, name='home'),
    path('login/',views.login,name ='login'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]