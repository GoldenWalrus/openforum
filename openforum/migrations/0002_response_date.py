# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('openforum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 2, 3, 50, 46, 956279, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
    ]
