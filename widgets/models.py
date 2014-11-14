# -*- coding: utf-8 -*-
from django.db import models

from entropy.base import (
    AttributeMixin, TextMixin, EnabledMixin, SlugMixin, TitleMixin
)
from templates.mixins import TemplateMixin

try:
    from images.mixins import ImageMixin
except ImportError:
    ImageMixin = object


class Widget(AttributeMixin, EnabledMixin, SlugMixin, TextMixin, TitleMixin,
             TemplateMixin, ImageMixin):
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
    # attr's
    # images


class WidgetAspect(models.Model):
    widget = models.ForeignKey('Widget', related_name='aspects')


class WidgetMailChimpSignup(WidgetAspect):
    '''
    For example, create a widget that sign's up to Mailchimp

    '''

    list_name = models.CharField(max_length=1024)
