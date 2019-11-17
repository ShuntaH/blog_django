from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.


class User(AbstractUser):
    pass


class Category(models.Model):
    """カテゴリー"""

    name = models.CharField('Category Name', max_length=255)
    created_at = models.DateTimeField('created_date', default=timezone.now)

    def __str__(self):
        return self.name


class Post(models.Model):
    """Articles"""

    title = models.CharField('Title', max_length=255)
    text = models.TextField('Content')
    created_at = models.DateTimeField('Created at', default=timezone.now)
    image = models.ImageField(upload_to='images')
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title
