from django.contrib import admin

from .models import Topic

# Manage the model through admin site
admin.site.register(Topic)