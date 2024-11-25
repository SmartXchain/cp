# rack/views.py

from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Rack, Inspection
from django.urls import reverse_lazy


class RackListView(ListView):
    model = Rack
    template_name = 'rack/rack_list.html'
    context_object_name = 'racks'


class RackDetailView(DetailView):
    model = Rack
    template_name = 'rack/rack_detail.html'
    context_object_name = 'rack'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inspections'] = self.object.inspections.all()  # Get inspection history
        return context


class RackCreateView(CreateView):
    model = Rack
    template_name = 'rack/rack_form.html'
    fields = ['rack_number', 'location', 'application_type', 'last_inspection_date', 'next_inspection_date', 'inspection_frequency', 'condition', 'inspector', 'notes', 'photo']
    success_url = reverse_lazy('rack_list')


class RackUpdateView(UpdateView):
    model = Rack
    template_name = 'rack/rack_form.html'
    fields = ['rack_number', 'location', 'application_type', 'last_inspection_date', 'next_inspection_date', 'inspection_frequency', 'condition', 'inspector', 'notes', 'photo']
    success_url = reverse_lazy('rack_list')


class InspectionCreateView(CreateView):
    model = Inspection
    template_name = 'rack/inspection_form.html'
    fields = ['inspection_date', 'inspector', 'condition', 'notes']

    def form_valid(self, form):
        form.instance.rack = get_object_or_404(Rack, pk=self.kwargs['rack_id'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rack'] = get_object_or_404(Rack, pk=self.kwargs['rack_id'])
        return context

    def get_success_url(self):
        return reverse_lazy('rack_detail', kwargs={'pk': self.kwargs['rack_id']})
