# -*- coding: utf-8 -*-
import eav

from django.db import models

from entropy.base import (
    AttributeMixin, TextMixin, EnabledMixin, SlugMixin, TitleMixin
)

from attrs.mixins import GenericAttrMixin
from templates.mixins import TemplateMixin

try:
    from images.mixins import ImageMixin
except ImportError:
    ImageMixin = object


# Widget Base Classes

class Widget(GenericAttrMixin, EnabledMixin, SlugMixin, TextMixin, TitleMixin,
             ImageMixin):
    '''
    A Widget is a contained module of functionality that is displayed within a
    Display.

    We add functionality by adding WidgetAspects

    '''

    # title
    # short_title
    # text
    # slug
    # enabled
    # images
    # attrs / name, value
    pass


class WidgetAspect(models.Model):

    widget = models.ForeignKey('Widget', related_name='aspects')


# Widgets


class WidgetMap(WidgetAspect, TitleMixin, SlugMixin, ImageMixin):
    '''
    An Image Based Map Widget with Points Of Interest.
    '''
    pass


class WidgetMapPOI(TextMixin, TitleMixin, SlugMixin):

    # title
    # short_title
    # slug
    # text

    widget_map = models.ForeignKey('WidgetMap', related_name='pios')

    x = models.IntegerField()
    y = models.IntegerField()
