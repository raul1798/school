# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20160425_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Klassam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=90, verbose_name=b'\xd0\x9a\xd0\xbb\xd0\xb0\xd1\x81\xd1\x81')),
            ],
        ),
        migrations.CreateModel(
            name='KlassamDoc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'media', null=True, verbose_name=b'\xd0\x94\xd0\xbe\xd0\xba\xd1\x83\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82')),
                ('doc', models.ForeignKey(verbose_name=b'\xd0\x9a \xd0\xba\xd0\xb0\xd0\xba\xd0\xbe\xd0\xbc\xd1\x83 \xd0\xba\xd0\xbb\xd0\xb0\xd1\x81\xd1\x81\xd1\x83', to='article.Klassam', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='historyimage',
            name='article',
        ),
        migrations.DeleteModel(
            name='History',
        ),
        migrations.DeleteModel(
            name='HistoryImage',
        ),
    ]
