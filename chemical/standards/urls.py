from django.urls import path
from . import views

urlpatterns = [
    path('', views.standard_list, name='standard_list'),
    path('<int:pk>/', views.standard_detail, name='standard_detail'),
    path('create/', views.standard_create, name='standard_create'),
]
