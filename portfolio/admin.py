from django.contrib import admin

# Register your models here.
# First we have to import the module 'Project'
from .models import Project

# Then we have to register it in the admin page
admin.site.register(Project)