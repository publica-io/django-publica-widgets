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
                ('list_title', models.CharField(max_length=50, null=True, verbose_name=b'List Item Title (used only in Definition Lists)')),
            ],
            options={
                'abstract': False,
            },
            bases=('widgets.widgetaspect', models.Model),
        ),
        migrations.AlterModelOptions(
            name='widget',
            options={'verbose_name': 'Content Widget', 'verbose_name_plural': 'Content Widgets'},
        ),
        migrations.AlterModelOptions(
            name='widgetmap',
            options={'verbose_name': 'Point Of Interest (POI) Map Widget', 'verbose_name_plural': 'Point Of Interest (POI) Map Widgets'},
        ),
        migrations.AlterModelOptions(
            name='widgetmappoi',
            options={'verbose_name': 'A Map Point Of Interest (POI)', 'verbose_name_plural': 'Map Points Of Interest (POI)'},
        ),
        migrations.AlterModelOptions(
            name='widgetmodal',
            options={'verbose_name': 'Content Widget with a Popup Modal', 'verbose_name_plural': 'Content Widgets with Popup Modals'},
        ),
    ]
