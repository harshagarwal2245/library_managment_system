from django.shortcuts import render
from shelf.models import Book
from .serializers import BookSerializer

def BookApiView(request):
    """This function is created to retriev
    all books from database"""
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return render(request, 'book_api_list.html', {'books': serializer.data})

