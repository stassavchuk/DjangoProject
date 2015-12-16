# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='full_name',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
    ]
