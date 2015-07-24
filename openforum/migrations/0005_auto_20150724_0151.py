# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openforum', '0004_question_questionnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='sticky',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
