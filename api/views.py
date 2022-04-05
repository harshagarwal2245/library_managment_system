from django.shortcuts import render
from shelf.models import Book
from .serializers import BookSerializer
from django.http import JsonResponse

def BookApiView(request):
    """This function is created to retriev
    all books from database"""
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return JsonResponse(serializer.data, safe=False)

