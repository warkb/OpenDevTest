from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import viewsets
from testapp.serializers import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookThemeViewSet(viewsets.ModelViewSet):
    queryset = BookTheme.objects.all()
    serializer_class = BookThemeSerializer

class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class BookOrderedViewSet(viewsets.ModelViewSet):
    queryset = BookOrdered.objects.all()
    serializer_class = BookOrderedSerializer