from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from tasks.views import dashboard  # Добавь этот импорт!

schema_view = get_schema_view(
   openapi.Info(
      title="Task Manager API",
      default_version='v1',
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

schema_view.security = [
    {
        'Bearer': []
    }
]

# ИСПРАВЛЕННЫЕ ПУТИ:
urlpatterns = [
    path('', dashboard, name='home'),             # Главная страница (http://127.0.0.1:8000/)
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]