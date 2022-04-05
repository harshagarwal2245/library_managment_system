from django import forms
from .models import Book

class BookAddForm(forms.ModelForm): 
    """Created form for adding a new book to the database. we had used meta model to check 
    which fields to be examined by the book model"""
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']