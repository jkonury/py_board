from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=80, verbose_name='게시판 이름')
    name = models.CharField(max_length=80)
    items_per_page = models.IntegerField(default=0, null=True, blank=True)
    is_admin = models.BooleanField(default=False, verbose_name='관리자용')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('entry-list', kwargs={'board_name': self.name})


class Category(models.Model):
    board = models.ForeignKey(Board, null=True)
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Entry(models.Model):
    parent = models.ForeignKey('Entry', null=True, blank=True)
    board = models.ForeignKey(Board, null=True, blank=True, on_delete=models.SET_NULL,)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL,)
    title = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, )
    user_name = models.CharField(max_length=20, blank=True)
    user_nick = models.CharField(max_length=20, blank=True)
    user_email = models.EmailField(max_length=50, blank=True)
    intro = models.CharField(max_length=200, blank=True)
    content = models.TextField(default='', blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    lasted_date = models.DateTimeField(auto_now=True)

    count = models.IntegerField(default=0)
    count_comment = models.IntegerField(default=0)

    ip = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('entry-detail', kwargs={'pk': self.pk})


class FlatPage(models.Model):
    class Meta:
        verbose_name = '페이지'
        verbose_name_plural = '페이지'
        ordering = ['-id']
    entry = models.OneToOneField(Entry)
    name = models.CharField(verbose_name='영문명', help_text='페이지 주소로 쓰일 영문명', max_length=50)