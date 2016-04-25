# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_delete_administacia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vchitel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='VchitelDoc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(null=True, upload_to=b'media')),
                ('doc', models.ForeignKey(to='article.Dpa', null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(max_length=90000),
        ),
    ]
