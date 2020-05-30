from django.db import models

class Pizza(models.Model):
    """Pizza class."""
    name = models.CharField(max_length=32)

    def __str__(self):
        """Return string."""
        return self.name

class Topping(models.Model):
    """Topping class."""
    name = models.CharField(max_length=32)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    def __str__(self):
        """Return string."""
        return self.name
