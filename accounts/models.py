from django.db import models
from django.conf import settings


class Profile(models.Model):
    """ 
    This class created a profile for the user we can add more fields to the profile
    as well but not added yet
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)