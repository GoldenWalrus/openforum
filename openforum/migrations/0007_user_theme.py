# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openforum', '0006_user_verification_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='theme',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]
