from django.contrib import admin
from django.urls import path, include
#from menu import views
from . import views

urlpatterns = [
    path('<int:storeID>/detail', views.detail, name="detail"),
    path('purchasing/<int:menu_id>/<int:store_id>/', views.purchasing, name="purchasing"),
    path('test/', views.checkAvailable, name='test')
]
