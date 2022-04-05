from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    """ 
    This class is used to customize the admin page. and to prepopulate the
    slug field with the title of the book. along with the date of creation
    which is used for sorting the books in the admin page. we had also customized
    the search fields in admin page
    """
    list_display = ('title', 'author', 'created_date', 'published_date')
    list_filter = ('created_date', 'published_date')
    search_fields = ('title', 'author')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('owner',)
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)

admin.site.register(Book, BookAdmin)
