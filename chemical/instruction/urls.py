# instruction/urls.py


from django.urls import path
from .views import InstructionListView, InstructionCreateView, InstructionUpdateView, get_parameters


urlpatterns = [
    path('', InstructionListView.as_view(), name='instruction_list'),
    path('create/', InstructionCreateView.as_view(), name='instruction_create'),
    path('<int:pk>/edit/', InstructionUpdateView.as_view(), name='instruction_update'),
    path('get_parameters/', get_parameters, name='get_parameters'),  # New endpoint
]
