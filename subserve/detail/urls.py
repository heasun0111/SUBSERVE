from django.contrib import admin
from django.urls import path, include
#from menu import views
from . import views

urlpatterns = [
    path('<int:storeID>/detail', views.detail, name="detail"),
    path('purchasing/', views.purchasing, name="purchasing")
]
