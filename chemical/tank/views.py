# tank/views.py

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Tank


class TankListView(ListView):
    model = Tank
    template_name = 'tank/tank_list.html'
    context_object_name = 'tanks'


class TankDetailView(DetailView):
    model = Tank
    template_name = 'tank/tank_detail.html'
    context_object_name = 'tank'


class TankCreateView(CreateView):
    model = Tank
    template_name = 'tank/tank_form.html'
    fields = [
        'tank_number', 'components_makeup', 'temperature_min', 'temperature_max',
        'uses_rectifier', 'rectifier_number', 'time_immersion_min', 'time_immersion_max',
        'test_required', 'process_description'
    ]
    success_url = reverse_lazy('tank_list')


class TankUpdateView(UpdateView):
    model = Tank
    template_name = 'tank/tank_form.html'
    fields = [
        'tank_number', 'components_makeup', 'temperature_min', 'temperature_max',
        'uses_rectifier', 'rectifier_number', 'time_immersion_min', 'time_immersion_max',
        'test_required', 'process_description'
    ]
    success_url = reverse_lazy('tank_list')
