# instruction/views.py

from django.views.generic import CreateView, UpdateView, ListView
from .models import Instruction
from .forms import InstructionForm
from django.urls import reverse_lazy

# instruction/views.py

from django.http import JsonResponse
from .models import CATEGORY_PARAMETERS

def get_parameters(request):
    category = request.GET.get('category')
    parameters = CATEGORY_PARAMETERS.get(category, "").split(', ')  # Return as list
    return JsonResponse({'parameters': parameters})


class InstructionListView(ListView):
    model = Instruction
    template_name = 'instruction/instruction_list.html'


class InstructionCreateView(CreateView):
    model = Instruction
    form_class = InstructionForm
    template_name = 'instruction/instruction_form.html'
    success_url = reverse_lazy('instruction_list')

class InstructionUpdateView(UpdateView):
    model = Instruction
    form_class = InstructionForm
    template_name = 'instruction/instruction_form.html'
    success_url = reverse_lazy('instruction_list')