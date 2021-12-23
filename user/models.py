from django.contrib.auth.models import AbstractBaseUser

from django.db import models

#user model with some added fields
class User(AbstractBaseUser):
    username = models.CharField( max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=15)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
