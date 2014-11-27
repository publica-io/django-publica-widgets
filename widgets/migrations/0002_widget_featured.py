# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='widget',
            name='featured',
            field=models.BooleanField(default=False, help_text=b'Feature this on the homepage'),
            preserve_default=True,
        ),
    ]
