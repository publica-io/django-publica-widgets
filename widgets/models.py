# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.loading import get_model

from polymorphic import PolymorphicModel

from entropy.base import (
    TextMixin, EnabledMixin, SlugMixin, TitleMixin
)

from attrs.mixins import GenericAttrMixin
from templates.mixins import TemplateMixin

try:
    from images.mixins import ImageMixin
except ImportError:
    ImageMixin = object


# Widget Base Classes

class Widget(PolymorphicModel, GenericAttrMixin, EnabledMixin, SlugMixin, TextMixin, TitleMixin,
             TemplateMixin, ImageMixin):
    '''
    A Widget is a contained module of functionality that is displayed within a
    Display.

    We add functionality by subclassing Widget into polymorphic implementations
    of Widget; the adding WidgetAspects or a light EAV implementation via the GenericAttrMixin
    to add custom fields in a 'name / value' style.

    '''

    # title
    # short_title
    # text
    # slug
    # enabled
    # images
    # attrs / name, value
    pass


class WidgetAspect(PolymorphicModel):

    widget = models.ForeignKey('Widget', related_name='aspects')


# Widgets


## Widget Map

class WidgetMap(Widget):
    '''
    An Image Based Map Widget with Points Of Interest.
    '''

    @property
    def pois(self):
        '''
        Return only the POIs Aspects of the Map.
        '''
        return self.aspects.filter(
            polymorphic_ctype=ContentType.objects.get_for_model(get_model('widgets.WidgetMapPOI')))


class WidgetMapPOI(WidgetAspect, TextMixin, TitleMixin, SlugMixin):
    '''
    Add a Point Of Interest to the Widget Map.
    '''

    # title
    # short_title
    # slug
    # text

    x = models.IntegerField()
    y = models.IntegerField()

## End Widget Map
