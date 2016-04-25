# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administacia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=90)),
                ('text', models.TextField(max_length=9000)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=90)),
                ('text', ckeditor.fields.RichTextField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Date publication')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=b'media', blank=True)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('article', models.ForeignKey(to='article.Article', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dpa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='DpaDoc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(null=True, upload_to=b'media')),
                ('doc', models.ForeignKey(to='article.Dpa', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=90)),
                ('text', models.TextField(max_length=9000)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Date publication')),
            ],
        ),
        migrations.CreateModel(
            name='HistoryImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=b'media', blank=True)),
                ('article', models.ForeignKey(to='article.History', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Zno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='ZnoDoc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(null=True, upload_to=b'media')),
                ('doc', models.ForeignKey(to='article.Zno', null=True)),
            ],
        ),
    ]
