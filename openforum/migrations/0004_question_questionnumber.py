# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openforum', '0003_auto_20150723_0332'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='questionnumber',
            field=models.IntegerField(default=0),
        ),
    ]
