# manual_method/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ManualMethodListView.as_view(), name='manualmethod_list'),
    path('<int:pk>/', views.ManualMethodDetailView.as_view(), name='manualmethod_detail'),
    path('create/', views.ManualMethodCreateView.as_view(), name='manualmethod_create'),
    path('<int:pk>/edit/', views.ManualMethodUpdateView.as_view(), name='manualmethod_update'),
]
