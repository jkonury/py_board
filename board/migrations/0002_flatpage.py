# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatPage',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, help_text='페이지 주소로 쓰일 영문명', verbose_name='영문명')),
                ('entry', models.OneToOneField(to='board.Entry')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name_plural': '페이지',
                'verbose_name': '페이지',
            },
        ),
    ]
