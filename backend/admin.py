from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_filter = ['close_date', 'is_complete', 'is_important']
    list_display = ('title', 'close_date', 'is_complete', 'is_important', 'id')
    search_fields = ['title']
