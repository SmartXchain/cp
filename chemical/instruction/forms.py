# instruction/forms.py


from django import forms
from .models import Instruction


class InstructionForm(forms.ModelForm):
    class Meta:
        model = Instruction
        fields = ['title', 'process_category', 'custom_description']

    def get_parameters_list(self):
        if self.instance and self.instance.parameters:
            return self.instance.parameters.split(', ')
        return []
