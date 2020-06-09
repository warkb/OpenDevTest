from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class BookThemeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookTheme
        fields = ['theme']

class BookSerializer(serializers.HyperlinkedModelSerializer):
    theme_code = BookThemeSerializer()
    class Meta:
        model = Book
        fields = ['author',
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
            'reader_code',
            'date'
        ]

class BookOrderedSerializer(serializers.HyperlinkedModelSerializer):
    order_code = OrderSerializer()
    book_code = BookSerializer()
    class Meta:
        model = BookOrdered
        fields = [
            'order_code',
            'book_code'
        ]
