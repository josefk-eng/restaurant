from django.urls import path
from . import views

urlpatterns = [
    path('',views.getData,name="nothing"),
    path('add/', views.addItem, name="add"),
]