# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181212_0440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
