from django.shortcuts import render,get_object_or_404
from .models import Book
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from .forms import BookAddForm
from django.utils.text import slugify
from django.utils import timezone

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


def is_authorized(user):
    """
    This function is used to check if the user is authorized to add a book. can be also done by decorator
    but we had used this function to make it more readable. 
    """
    return user.is_staff or user.is_superuser




def AddPost(request):
    """ 
    This function is used to add a new book to the database. which takes in used form which 
    we had created in forms.py and then we had used the model to add the data to the database.
    and we had used is_authorized function to check if the user is authorized to add a book.
    we had not directly committed the data to the database as we need to admin user to do that.
    """
    if request.method=='POST':
        form=BookAddForm(request.POST)
        if form.is_valid():
            book=form.save(commit=False)
            book.owner=request.user
            book.slug=slugify(form.cleaned_data['title'])
            book.published_date=timezone.now()
            if is_authorized(request.user):
                book.save()
                return render(request,'shelf/book_added.html',{'book':book})
            else:
                return render(request,'shelf/not_allowed.html')
    else:
        form=BookAddForm()
    return render(request,'shelf/add.html',{'form':form})


def delbook(request,book_id):
    """ 
    this allows Admin to delete the book from database
    it accepts id object as a unique parameter to find the
    book
    """
    book=get_object_or_404(Book,id=book_id)
    if is_authorized(request.user):
        book.delete()
        return render(request,'shelf/book_deleted.html',{'book':book})
    else:
        return render(request,'shelf/not_allowed.html')


def update_book(request,book_id):
    """ 
    this allows Admin to update the book from database
    we take book_id as a parameter to uniquely identify the
    record and pass it as a instance to form so that it can
    poppulate the field
    """
    book=get_object_or_404(Book,id=book_id)
    if is_authorized(request.user):
        if request.method=='POST':
            form=BookAddForm(request.POST,instance=book)
            if form.is_valid():
                book=form.save(commit=False)
                book.owner=request.user
                book.slug=slugify(form.cleaned_data['title'])
                book.published_date=timezone.now()
                if is_authorized(request.user):
                    book.save()
                    return render(request,'shelf/book_updated.html',{'book':book})
                else:
                    return render(request,'shelf/not_allowed.html')
        else:
            form=BookAddForm(instance=book)
        return render(request,'shelf/update.html',{'form':form})


