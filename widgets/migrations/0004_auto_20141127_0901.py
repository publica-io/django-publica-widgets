# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0003_auto_20141127_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widget',
            name='preview_template',
            field=models.ForeignKey(related_name='widgets_widget_preview_templates', blank=True, to='templates.Template', help_text=b'Optionally choose a Listing Template that will be used in List Views', null=True, verbose_name=b'Listing/Preview Template'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='widget',
            name='template',
            field=models.ForeignKey(related_name='widgets_widget_templates', blank=True, to='templates.Template', help_text=b'Choose a template to render this content', null=True),
            preserve_default=True,
        ),
    ]
