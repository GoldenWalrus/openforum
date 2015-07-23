# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openforum', '0002_response_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='board',
            field=models.ForeignKey(default=0, to='openforum.Board'),
            preserve_default=False,
        ),
    ]
