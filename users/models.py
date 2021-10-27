from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField( verbose_name='email', max_length=255, unique=True),
    # username = models.CharField(max_length=15)
    posts = models.ForeignKey('dinnerdash.Recipe', related_name='user',on_delete=models.CASCADE)
    likes = models.IntegerField()
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
