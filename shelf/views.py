from django.shortcuts import render,get_object_or_404
from .models import Book
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger


def book_list(request):
    """
    This function returns a list of all books in the database.
    """
    books = Book.objects.all()
    paginator = Paginator(books, 3)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'shelf/book_list.html', {'books': books,'page':page})


def book_detail(request, year,month,day,book):
    """
    This function returns a single book from the database so for that we
    need a unique key we had used here created_date. and we had used slug
    for the url
    """
    book = get_object_or_404(Book, slug=book,
                             created_date__year=year,
                             created_date__month=month,
                             created_date__day=day)
    return render(request, 'shelf/book_detail.html', {'book': book})
