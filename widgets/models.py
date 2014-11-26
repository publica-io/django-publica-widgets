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

    @property
    def modal(self):
        return self.content_object


# WidgetMap
class WidgetMap(Widget):
    '''
    An Image Based Map Widget with Points Of Interest.

    '''

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
