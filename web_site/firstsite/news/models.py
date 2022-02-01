from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser


class NewUser(User):
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.FileField(upload_to='img/users/', null=True, blank=True)


class Comments(models.Model):
    text = models.TextField()
    head_news = models.ForeignKey('HeadNews', on_delete=models.CASCADE, verbose_name='HeadNews', null=True,
                                  blank=True, related_name='comments_head')
    news = models.ForeignKey('News', on_delete=models.CASCADE, verbose_name='News', null=True, blank=True,
                             related_name='comments_news')
    user_name = models.ForeignKey('NewUser', on_delete=models.PROTECT, verbose_name="NewUser", null=True)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', 'user_name']


class HeadNews(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')
    text = models.TextField()
    date = models.DateTimeField()
    image = models.FileField(upload_to='img/')
    announcement = models.TextField(max_length=300)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Category")
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article', kwargs={'post_slug': self.slug})

    class Meta:
        ordering = ['-date', 'name']


class News(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')
    text = models.TextField()
    date = models.DateTimeField()
    announcement = models.TextField(max_length=200)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('news', kwargs={'post_slug': self.slug})

    def get_date(self):
        return self.date

    class Meta:
        ordering = ['-date', 'name']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Category")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})
