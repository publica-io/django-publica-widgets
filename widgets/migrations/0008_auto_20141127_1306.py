# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0007_auto_20141127_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widgetlistaspect',
            name='widget',
            field=models.ForeignKey(to='widgets.Widget'),
            preserve_default=True,
        ),
    ]
