# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=80, verbose_name='게시판 이름')),
                ('name', models.CharField(max_length=80)),
                ('items_per_page', models.IntegerField(null=True, default=0, blank=True)),
                ('is_admin', models.BooleanField(verbose_name='관리자용', default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('board', models.ForeignKey(null=True, to='board.Board')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200, blank=True)),
                ('user_name', models.CharField(max_length=20, blank=True)),
                ('user_nick', models.CharField(max_length=20, blank=True)),
                ('user_email', models.EmailField(max_length=50, blank=True)),
                ('intro', models.CharField(max_length=200, blank=True)),
                ('content', models.TextField(default='', blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('lasted_date', models.DateTimeField(auto_now=True)),
                ('count', models.IntegerField(default=0)),
                ('count_comment', models.IntegerField(default=0)),
                ('ip', models.GenericIPAddressField(null=True, blank=True)),
                ('board', models.ForeignKey(to='board.Board', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL)),
                ('category', models.ForeignKey(to='board.Category', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL)),
                ('parent', models.ForeignKey(to='board.Entry', blank=True, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL)),
            ],
        ),
    ]
