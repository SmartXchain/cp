from django.urls import path
from . import views

urlpatterns = [
    path('', views.StandardListView.as_view(), name='standards_list'),
    path('<int:pk>/', views.StandardDetailView.as_view(), name='standard_detail'),
    path('create/', views.StandardCreateView.as_view(), name='standard_create'),
    path('<int:pk>/edit/', views.StandardUpdateView.as_view(), name='standard_update'),
    path('<int:standard_id>/inspections/add/', views.InspectionCreateView.as_view(), name='inspection_create'),
    path('inspections/<int:pk>/edit/', views.InspectionUpdateView.as_view(), name='inspection_update'),

    # ProcessStep URLs
    path('<int:standard_id>/process_steps/add/', views.ProcessStepCreateView.as_view(), name='process_step_create'),
    path('process_steps/<int:pk>/edit/', views.ProcessStepUpdateView.as_view(), name='process_step_update'),
]
