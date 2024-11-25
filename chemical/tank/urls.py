# tank/urls.py


from django.urls import path
from . import views

urlpatterns = [
    path('', views.TankListView.as_view(), name='tank_list'),
    path('<int:pk>/', views.TankDetailView.as_view(), name='tank_detail'),
    path('create/', views.TankCreateView.as_view(), name='tank_create'),
    path('<int:pk>/edit/', views.TankUpdateView.as_view(), name='tank_update'),
]
