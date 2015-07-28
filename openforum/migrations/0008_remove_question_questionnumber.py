# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openforum', '0007_user_theme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='questionnumber',
        ),
    ]
