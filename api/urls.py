from  django.urls import path
from .views import BookApiView

urlpatterns=[
    path('', BookApiView, name='book_api_list'),
]