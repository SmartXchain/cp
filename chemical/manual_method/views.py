# manual_method/views.py


from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import ManualMethod


class ManualMethodListView(ListView):
    model = ManualMethod
    template_name = 'manual_method/manualmethod_list.html'
    context_object_name = 'manual_methods'


class ManualMethodDetailView(DetailView):
    model = ManualMethod
    template_name = 'manual_method/manualmethod_detail.html'
    context_object_name = 'manual_method'


class ManualMethodCreateView(CreateView):
    model = ManualMethod
    template_name = 'manual_method/manualmethod_form.html'
    fields = ['method_number', 'description', 'process_type', 'temperature_min', 'temperature_max', 'time_immersion_min', 'time_immersion_max', 'test_required']
    success_url = reverse_lazy('manualmethod_list')


class ManualMethodUpdateView(UpdateView):
    model = ManualMethod
    template_name = 'manual_method/manualmethod_form.html'
    fields = ['method_number', 'description', 'process_type', 'temperature_min', 'temperature_max', 'time_immersion_min', 'time_immersion_max', 'test_required']
    success_url = reverse_lazy('manualmethod_list')
