from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Standard, Inspection, ProcessStep


class StandardListView(ListView):
    model = Standard
    template_name = 'standards/standards_list.html'
    context_object_name = 'standards'


class StandardDetailView(DetailView):
    model = Standard
    template_name = 'standards/standard_detail.html'
    context_object_name = 'standard'


class StandardCreateView(CreateView):
    model = Standard
    template_name = 'standards/standard_form.html'
    fields = ['name', 'description', 'revision', 'author', 'class_field', 'type', 'process']
    success_url = reverse_lazy('standards_list')


class StandardUpdateView(UpdateView):
    model = Standard
    template_name = 'standards/standard_form.html'
    fields = ['name', 'description', 'revision', 'author', 'class_field', 'type', 'process']
    success_url = reverse_lazy('standards_list')


class InspectionCreateView(CreateView):
    model = Inspection
    template_name = 'standards/inspection_form.html'
    fields = ['name', 'acceptance_criteria', 'paragraph_section', 'sampling_plan']

    def form_valid(self, form):
        form.instance.standard = get_object_or_404(Standard, pk=self.kwargs['standard_id'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['standard_id'] = self.kwargs['standard_id']  # Pass standard_id to template context
        return context

    def get_success_url(self):
        return reverse_lazy('standard_detail', kwargs={'pk': self.kwargs['standard_id']})


class InspectionUpdateView(UpdateView):
    model = Inspection
    template_name = 'standards/inspection_form.html'
    fields = ['name', 'acceptance_criteria', 'paragraph_section', 'sampling_plan']

    def get_success_url(self):
        return reverse_lazy('standard_detail', kwargs={'pk': self.object.standard.pk})

# ProcessStep Views


class ProcessStepCreateView(CreateView):
    model = ProcessStep
    template_name = 'standards/process_step_form.html'
    fields = ['step_number', 'instruction', 'operator', 'date']

    def form_valid(self, form):
        form.instance.standard = get_object_or_404(Standard, pk=self.kwargs['standard_id'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['standard_id'] = self.kwargs['standard_id']  # Ensure standard_id is in context
        return context

    def get_success_url(self):
        return reverse_lazy('standard_detail', kwargs={'pk': self.kwargs['standard_id']})


class ProcessStepUpdateView(UpdateView):
    model = ProcessStep
    template_name = 'standards/process_step_form.html'
    fields = ['step_number', 'instruction', 'operator', 'date']

    def get_success_url(self):
        return reverse_lazy('standard_detail', kwargs={'pk': self.object.standard.pk})
