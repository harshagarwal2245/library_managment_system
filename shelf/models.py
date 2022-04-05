from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse



class Book(models.Model):
    """created database model for storing book information"""
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    slug=models.SlugField(max_length=200, unique_for_date='created_date')
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shelf:book_detail', args=[self.created_date.year,
                                            self.created_date.month,
                                            self.created_date.day,
                                            self.slug])
    
    