# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0004_auto_20141127_0901'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='widgetmodal',
            options={'verbose_name': 'Content Widget with a Popup Modal', 'verbose_name_plural': 'Content Widgets with Popup Modals'},
        ),
        migrations.AlterField(
            model_name='widgetlist',
            name='type',
            field=models.CharField(default=b'ul', max_length=2, choices=[(b'ol', b'ordered'), (b'ul', b'un-ordered'), (b'dl', b'definition')]),
            preserve_default=True,
        ),
    ]
