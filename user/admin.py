from django.contrib import admin

from . models import User

#register user model with admin
admin.site.register(User)