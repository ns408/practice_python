from django.shortcuts import render

from .models import Pizza

def index(request):
    """Home page for pizzas."""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """Display all pizzas."""
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)
