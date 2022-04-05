from django.urls import path
from .views import *

app_name='shelf'

urlpatterns=[
    path('', book_list, name='book_list'),#book_list is the name of the function in views.py
    path('<int:year>/<int:month>/<int:day>/<slug:book>/', book_detail, name='book_detail'),
    path('add/', AddPost, name='addpost'),
    
]