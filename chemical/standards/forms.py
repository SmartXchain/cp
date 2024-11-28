# standards/forms.py
from django import forms
from .models import ProcessStep
from instruction.models import Instruction


class ProcessStepForm(forms.ModelForm):
    instruction = forms.ModelChoiceField(queryset=Instruction.objects.all(), required=True)

    class Meta:
        model = ProcessStep
        fields = ['step_number', 'instruction', 'operator', 'date']
