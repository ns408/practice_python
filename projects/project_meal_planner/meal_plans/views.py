from django.shortcuts import render

def index(request):
    """Home page for meal_plans."""
    return render(request, 'meal_plans/index.html')
