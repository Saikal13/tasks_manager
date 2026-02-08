from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task
from django.utils import timezone

# Сериализатор для регистрации
class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirm')

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Пароли не совпадают")
        if len(data['password']) < 8:
            raise serializers.ValidationError("Пароль слишком короткий")
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user

# Сериализатор для задач
class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = '__all__'

    def validate_deadline(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Дедлайн не может быть в прошлом!")
        return value