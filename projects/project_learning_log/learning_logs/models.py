from django.db import models

# Create your models here.
# Structure: User will create number of topics.
# Entries tied to a topic and displayed as text.

class Topic(models.Model):
    """A topic for user"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string representation of the model."""
        return self.text