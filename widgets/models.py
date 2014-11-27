# -*- coding: utf-8 -*-
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.loading import get_model
from django.utils.functional import cached_property

from polymorphic import PolymorphicModel

from entropy.mixins import (
    TextMixin, EnabledMixin, LinkURLMixin, SlugMixin, TitleMixin
)

from attrs.mixins import GenericAttrMixin
from templates.mixins import TemplateMixin

from .settings import MAP_POI_ACTIVITIES, MAP_POI_VENUES

try:
    from images.mixins import ImageMixin
except ImportError:
    ImageMixin = object

# Widget Base Classes

class Widget(PolymorphicModel, GenericAttrMixin, EnabledMixin, SlugMixin,
             TextMixin, TitleMixin, TemplateMixin, ImageMixin):
    '''
    A Widget is a contained module of functionality that is displayed within a
    Display.

    We add functionality by subclassing Widget into polymorphic implementations
    of Widget; the adding WidgetAspects or a light EAV implementation via the
    GenericAttrMixin to add custom fields in a 'name / value' style.

    '''

    # title
    # short_title
    # text
    # slug
    # enabled
    # images
    # attrs / name, value
    
    featured = models.BooleanField(
        default=False,
        help_text='Feature this on the homepage'
    )

    class Meta:
        verbose_name = 'Content Widget'
        verbose_name_plural = 'Content Widgets'

    @property
    def links(self):
        return [widget_link.link for widget_link in self.aspects.filter(
            polymorphic_ctype=ContentType.objects.get_for_model(
                get_model('widgets.WidgetLinkAspect')
            )
        )]

    @property
    def link(self):
        try:
            return self.links[0]
        except IndexError:
            return None


class WidgetAspect(PolymorphicModel, TitleMixin, TextMixin, SlugMixin, ImageMixin):

    widget = models.ForeignKey('Widget', related_name='aspects')


###
# Widgets
###


# Widget link

class WidgetLinkAspect(WidgetAspect):
    '''
    Create a linkage to a menus.Link
    '''

    link = models.ForeignKey('menus.Link')



# Widget With Modal

class WidgetModal(Widget):

    content_type = models.ForeignKey(
        'contenttypes.ContentType',
        limit_choices_to={'model__in': ['modal',]},
    )
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'Content Widget with a Popup Modal Window'
        verbose_name_plural = 'Content Widgets with Popup Modal Windows'

    @property
    def modal(self):
        return self.content_object


# WidgetMap
class WidgetMap(Widget):
    '''
    An Image Based Map Widget with Points Of Interest.

    '''

    class Meta:
        verbose_name = 'Point Of Interest (POI) Map Widget'
        verbose_name_plural = 'Point Of Interest (POI) Map Widgets'

    @cached_property
    def pois(self):
        '''
        Return only the POIs Aspects of the Map.

        '''

        return self.aspects.filter(
            polymorphic_ctype=ContentType.objects.get_for_model(
                get_model('widgets.WidgetMapPOI')
            )
        )


class WidgetMapPOI(WidgetAspect):
    '''
    Add a Point Of Interest to the Widget Map.

    '''

    # widget
    # title
    # short_title
    # slug
    # text

    activity = models.CharField(choices=MAP_POI_ACTIVITIES, max_length=50)
    venue = models.CharField(choices=MAP_POI_VENUES, max_length=50)

    x = models.IntegerField()
    y = models.IntegerField()

    class Meta:
        verbose_name = 'A Map Point Of Interest (POI)'
        verbose_name_plural = 'Map Points Of Interest (POI)'


# Widget List
class WidgetList(Widget):

    type = models.CharField(choices=(
            ('ol', 'ordered'),
            ('ul', 'un-ordered'),
            ('dl', 'definition'),
        ),
        max_length=2
    )

    class Meta:
        verbose_name = 'List Widget'
        verbose_name_plural = 'List Widgets w/ Numbered Items'

    @cached_property
    def items(self):
        '''
        Return only the List Aspects of the Grid.

        '''

        return self.aspects.filter(
            polymorphic_ctype=ContentType.objects.get_for_model(
                get_model('widgets.WidgetListAspect')
            )
        )

class WidgetListAspect(models.Model):

    widget = models.ForeignKey('Widget')

    title = models.CharField(
        'List Item Title (used only in Definition Lists)',
        max_length=50,
        blank=True)

    definition = models.CharField(
        'List Item Value / Defintion',
        max_length=1024)
