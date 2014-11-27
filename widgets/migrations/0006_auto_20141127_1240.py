# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0005_auto_20141127_1231'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='widgetlistaspect',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='widgetlistaspect',
            name='order',
            field=models.PositiveIntegerField(default=0, blank=True),
            preserve_default=True,
        ),
    ]
