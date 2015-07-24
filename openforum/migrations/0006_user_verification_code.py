# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openforum', '0005_auto_20150724_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verification_code',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
