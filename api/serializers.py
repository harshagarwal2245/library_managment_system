from rest_framework import serializers
from shelf.models import Book

class BookSerializer(serializers.ModelSerializer):
    """This class is created to serialize
    the data from database into json format"""
    class Meta:
        model = Book
        fields = ('id','title','author','published_date')