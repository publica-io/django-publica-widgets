# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import entropy.mixins
import images.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('templates', '__first__'),
        ('menus', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(default=b'', blank=True)),
                ('title', models.CharField(max_length=255)),
                ('short_title', models.CharField(max_length=255, blank=True)),
                ('slug', models.SlugField(max_length=255)),
                ('enabled', models.BooleanField(default=False, db_index=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(entropy.mixins.BaseSlugMixin, models.Model, images.mixins.ImageMixin),
        ),
        migrations.CreateModel(
            name='WidgetAspect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(default=b'', blank=True)),
                ('title', models.CharField(max_length=255)),
                ('short_title', models.CharField(max_length=255, blank=True)),
                ('slug', models.SlugField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(entropy.mixins.BaseSlugMixin, models.Model, images.mixins.ImageMixin),
        ),
        migrations.CreateModel(
            name='WidgetLinkAspect',
            fields=[
                ('widgetaspect_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='widgets.WidgetAspect')),
                ('link', models.ForeignKey(to='menus.Link')),
            ],
            options={
                'abstract': False,
            },
            bases=('widgets.widgetaspect',),
        ),
        migrations.CreateModel(
            name='WidgetMap',
            fields=[
                ('widget_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='widgets.Widget')),
            ],
            options={
                'abstract': False,
            },
            bases=('widgets.widget',),
        ),
        migrations.CreateModel(
            name='WidgetMapPOI',
            fields=[
                ('widgetaspect_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='widgets.WidgetAspect')),
                ('activity', models.CharField(max_length=50, choices=[(b'place-see', b'Place to See'), (b'place-eat', b'Place to Eat')])),
                ('venue', models.CharField(max_length=50, choices=[(b'bar', b'Bar'), (b'cafe', b'Coffee'), (b'food', b'Food')])),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=('widgets.widgetaspect',),
        ),
        migrations.CreateModel(
            name='WidgetModal',
            fields=[
                ('widget_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='widgets.Widget')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
            bases=('widgets.widget',),
        ),
        migrations.AddField(
            model_name='widgetaspect',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_widgets.widgetaspect_set', editable=False, to='contenttypes.ContentType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='widgetaspect',
            name='widget',
            field=models.ForeignKey(related_name='aspects', to='widgets.Widget'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='widget',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_widgets.widget_set', editable=False, to='contenttypes.ContentType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='widget',
            name='preview_template',
            field=models.ForeignKey(related_name='widgets_widget_preview_templates', blank=True, to='templates.Template', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='widget',
            name='template',
            field=models.ForeignKey(related_name='widgets_widget_templates', blank=True, to='templates.Template', null=True),
            preserve_default=True,
        ),
    ]
