# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0002_widget_featured_on_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='WidgetList',
            fields=[
                ('widget_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='widgets.Widget')),
                ('type', models.CharField(max_length=2, choices=[(b'ol', b'ordered'), (b'ul', b'un-ordered'), (b'dl', b'definition')])),
            ],
            options={
                'abstract': False,
            },
            bases=('widgets.widget',),
        ),
        migrations.CreateModel(
            name='WidgetListAspect',
            fields=[
                ('widgetaspect_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='widgets.WidgetAspect')),
                ('list_title', models.CharField(max_length=50, verbose_name=b'List Item Title (used only in Definition Lists)')),
                ('definition', models.CharField(max_length=1024, verbose_name=b'List Item Value / Defintion')),
            ],
            options={
                'abstract': False,
            },
            bases=('widgets.widgetaspect', models.Model),
        ),
    ]
