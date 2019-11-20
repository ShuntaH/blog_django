from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Post, Category

# Register your models here.


admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Post)

