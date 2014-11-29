# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0008_auto_20141127_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widgetlistaspect',
            name='definition',
            field=models.TextField(verbose_name=b'List Item Value / Defintion'),
            preserve_default=True,
        ),
    ]
