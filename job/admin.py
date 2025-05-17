from django.contrib import admin

from .models import Job
from .models import Category

admin.site.register(Job)
admin.site.register(Category)