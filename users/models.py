from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField( verbose_name='email', max_length=255, unique=True)
    # username = models.CharField(max_length=15)
    likes = models.IntegerField(default=0)
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
