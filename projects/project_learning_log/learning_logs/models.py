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

# Defining the Entry Model
# Model for entries users can make in the learning logs.
# Each entry needs to be associated with a particular topic.
# Many-to-one relationship: many entries associated with one topic.

class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."
