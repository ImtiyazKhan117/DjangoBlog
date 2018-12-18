# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181212_0438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='email',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='subject',
        ),
    ]
