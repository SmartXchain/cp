# rack/urls.py


from django.urls import path
from . import views

urlpatterns = [
    path('', views.RackListView.as_view(), name='rack_list'),
    path('<int:pk>/', views.RackDetailView.as_view(), name='rack_detail'),
    path('create/', views.RackCreateView.as_view(), name='rack_create'),
    path('<int:pk>/edit/', views.RackUpdateView.as_view(), name='rack_update'),
    path('<int:rack_id>/add_inspection/', views.InspectionCreateView.as_view(), name='add_inspection'),
]
