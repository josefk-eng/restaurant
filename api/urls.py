from django.urls import path
from . import views

urlpatterns = [
    path('',views.getData,name="nothing"),
    path('add/', views.addItem, name="add"),
    path('addMenu', views.addMenu, name="addMenu"),
    path('menus', views.getAllMenus,name='menus'),
]
