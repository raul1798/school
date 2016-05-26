# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20160429_1250'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '\u041d\u043e\u0432\u043e\u0441\u0442\u044c', 'verbose_name_plural': '\u041d\u043e\u0432\u043e\u0441\u0442\u0438'},
        ),
        migrations.AlterModelOptions(
            name='articleimage',
            options={'verbose_name': '\u0424\u043e\u0442\u043e \u0434\u043b\u044f \u043d\u043e\u0432\u043e\u0441\u0442\u0438', 'verbose_name_plural': '\u0424\u043e\u0442\u043e \u0434\u043b\u044f \u043d\u043e\u0432\u043e\u0441\u0442\u0438'},
        ),
        migrations.AlterModelOptions(
            name='dpa',
            options={'verbose_name': '\u0414\u041f\u0410', 'verbose_name_plural': '\u0414\u041f\u0410'},
        ),
        migrations.AlterModelOptions(
            name='dpadoc',
            options={'verbose_name': '\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442 \u0434\u043b\u044f \u0414\u041f\u0410', 'verbose_name_plural': '\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b \u0434\u043b\u044f \u0414\u041f\u0410'},
        ),
        migrations.AlterModelOptions(
            name='klassam',
            options={'verbose_name': '\u041a\u043b\u0430\u0441\u0441\u0430\u043c', 'verbose_name_plural': '\u041a\u043b\u0430\u0441\u0441\u0430\u043c'},
        ),
        migrations.AlterModelOptions(
            name='klassamdoc',
            options={'verbose_name': '\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b \u043a\u043b\u0430\u0441\u0441\u0430\u043c', 'verbose_name_plural': '\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b \u043a\u043b\u0430\u0441\u0441\u0430\u043c'},
        ),
        migrations.AlterModelOptions(
            name='vchitel',
            options={'verbose_name': '\u0423\u0447\u0438\u0442\u0435\u043b\u044e', 'verbose_name_plural': '\u0423\u0447\u0438\u0442\u0435\u043b\u044e'},
        ),
        migrations.AlterModelOptions(
            name='vchiteldoc',
            options={'verbose_name': '\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442 \u0443\u0447\u0438\u0442\u0435\u043b\u044e', 'verbose_name_plural': '\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b \u0443\u0447\u0438\u0442\u0435\u043b\u044e'},
        ),
        migrations.AlterModelOptions(
            name='zno',
            options={'verbose_name': '\u0417\u041d\u041e', 'verbose_name_plural': '\u0417\u041d\u041e'},
        ),
        migrations.AlterModelOptions(
            name='znodoc',
            options={'verbose_name': '\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442 \u0434\u043b\u044f \u0417\u041d\u041e', 'verbose_name_plural': '\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b \u0434\u043b\u044f \u0417\u041d\u041e'},
        ),
    ]
