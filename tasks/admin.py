from django.contrib import admin
from .models import Task  # Импортируем твою модель

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Эти колонки будут видны в списке админки
    list_display = ('title', 'owner', 'status', 'deadline', 'created_at')
    # По этим полям можно будет фильтровать
    list_filter = ('status', 'owner', 'deadline')
    # По этим полям будет работать поиск в админке
    search_fields = ('title', 'description')