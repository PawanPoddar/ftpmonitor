from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="ftpMonitor"),
    path('index', views.index, name="index"),
    path('allabout', views.allabout, name="allabout"),
    path('fileSearch',views.fileSearch, name="fileSearch"),
    path('searchDate',views.searchByDate,name="dateSearch"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('register', views.register, name="register"),
    path('realTime', views.realTime, name="realTime"),
    path('twoDates',views.twoDates,name="twodates"),
    path('timeInterval',views.timeInterval,name="Interval"),
    path('bytimeDate',views.bytimeDate,name="searchByDateTime"),

]
