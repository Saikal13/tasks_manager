from rest_framework import viewsets, generics, filters, permissions
from django.contrib.auth.models import User
from .models import Task
from .serializers import TaskSerializer, RegisterSerializer
from django.shortcuts import render


# Вьюха для регистрации
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

# Вьюха для задач
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated] # Только для вошедших
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['created_at']

    def get_queryset(self):
        # Видим только свои задачи
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


def index_view(request):
    return render(request, 'tasks/index.html')

def dashboard(request):
    return render(request, 'tasks/index.html')