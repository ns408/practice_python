from django.contrib import admin

from .models import Topic, Entry

# Manage the model through admin site
admin.site.register(Topic)

# Register the Entry Model
admin.site.register(Entry)