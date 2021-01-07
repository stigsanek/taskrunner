import json

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Task
from .permissions import IsOwner
from .serializers import TaskSerializer, UserSerializer


@ensure_csrf_cookie
@api_view(['GET'])
def set_csrf_token(request, format=None):
    return Response({'details': 'CSRF cookie set'}, status=200)


@api_view(['POST'])
def auth(request, format=None):
    if request.user.is_authenticated:
        return Response({'details': 'You are already signed in'}, status=200)
    else:
        data = json.loads(request.body)

        try:
            username = data['username']
            password = data['password']
        except KeyError:
            return Response({'errors': {'__all__': 'Please enter username and password'}}, status=400)

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({'details': 'Success'}, status=200)

        return Response({'details': 'Invalid credentials'}, status=200)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'tasks': reverse('backend:task-list', request=request, format=format),
        'user': reverse('backend:user-detail', request=request, format=format)
    })


class TaskList(generics.ListCreateAPIView):
    filterset_fields = ['close_date', 'is_complete', 'is_important']
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user.pk).order_by('close_date')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user.pk).order_by('close_date')


class UserDetail(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)
