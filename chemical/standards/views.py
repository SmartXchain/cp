from django.shortcuts import get_object_or_404, render, redirect
from .models import Standard
from .forms import StandardForm


def standard_list(request):
    items = Standard.objects.all()
    return render(request, 'standards/standard_list.html', {'items': items})


def standard_create(request):
    if request.method == 'POST':
        form = StandardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('standard_list')
    else:
        form = StandardForm()
    return render(request, 'standards/standard_form.html', {'form': form})


def standard_detail(request, pk):
    item = get_object_or_404(Standard, pk=pk)
    return render(request, 'standards/standard_detail.html', {'item': item})
