from django.contrib import admin
from .models import Tasks

@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'completed', 'due_date', 'priority']
    list_filter = ['completed', 'priority']
    search_fields = ['title', 'description']
