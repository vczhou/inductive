from django.contrib import admin

# Register your models here.
from .models import Chapter, Question

admin.site.register(Chapter)
admin.site.register(Question)