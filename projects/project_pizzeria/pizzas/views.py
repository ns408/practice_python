from django.shortcuts import render

def index(request):
    """Home page for pizzas."""
    return render(request, 'pizzas/index.html')
