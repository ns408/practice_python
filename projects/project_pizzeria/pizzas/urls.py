"""Defines URL patterns for Pizzas."""

from django.urls import path
from . import views

app_name = 'pizzas'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Show all pizzas
    path('pizzas/', views.pizzas, name='pizzas'),
    # Show pizza's toppings
    path('pizzas/<int:pizza_id>', views.pizza, name='pizza'),
]
