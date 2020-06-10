from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['pk', 'url', 'name']

class BookThemeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookTheme
        fields = ['pk','theme']

class BookSerializer(serializers.HyperlinkedModelSerializer):
    theme_code = BookThemeSerializer()
    class Meta:
        model = Book
        fields = ['pk',
                  'author',
                  'title',
                  'publisher',
                  'published_year',
                  'price',
                  'theme_code'
                  ]

class ReaderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reader
        fields = [
            'pk',
            'surname',
            'name',
            'fathername',
            'phone'
        ]

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    reader_code = ReaderSerializer()
    class Meta:
        model = Order
        fields = [
            'pk',
            'reader_code',
            'date'
        ]

class BookOrderedSerializer(serializers.HyperlinkedModelSerializer):
    order_code = OrderSerializer()
    book_code = BookSerializer()
    class Meta:
        model = BookOrdered
        fields = [
            'pk',
            'order_code',
            'book_code'
        ]
