# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20181212_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='email',
            field=models.CharField(default=datetime.datetime(2018, 12, 16, 5, 11, 5, 215989, tzinfo=utc), max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='snippet',
            name='subject',
            field=models.CharField(default=datetime.datetime(2018, 12, 16, 5, 11, 19, 20011, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
