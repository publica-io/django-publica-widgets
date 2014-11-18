#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-publica-widgets
------------

Tests for `django-publica-widgets` models module.
"""

import os
import shutil
import unittest
import random

from django.contrib.contenttypes.models import ContentType

from widgets import models
from attrs.models import Attribute


class TestWidgetAttrs(unittest.TestCase):

    def setUp(self):
        
        self.widget = models.Widget(
            title = 'foo',
            slug = 'foo')
        self.widget.save()
        self.widget['foo'] = 'bar'


    def test_attr(self):
        '''
        Test that the attr 'foo' is saved on the widget object.
        '''
        self.assertEqual(self.widget['foo'], 'bar')

    def test_attr_attribute(self):
        '''
        Test that the same attr is saved in the Attribute model
        and is accessbile via a query.
        '''
        self.attr = Attribute.objects.get(
            content_type = ContentType.objects.get_for_model(self.widget),
            object_id = self.widget.id,
            name = 'foo')
        self.assertEqual(self.attr.name, 'foo')
        self.assertEqual(self.attr.value, 'bar')

    def tearDown(self):
        Attribute.objects.all().delete()
        models.Widget.objects.all().delete()



class TestWidgetMap(unittest.TestCase):

    def setUp(self):
        
        self.widget_map = models.WidgetMap(
            title = 'A Nice Map',
            slug = 'a-nice-map')
        self.widget_map.save()
        
        # exercise EAV
        self.widget_map['byline'] = 'A Nice Map of Nice Points of Interest'

        for i in range(10):

            widget_poi = models.WidgetMapPOI(
                widget = self.widget_map,
                title = 'POI %s' % i,
                slug = 'poi-%s' % i,
                x = random.randint(0, 100),
                y = random.randint(0, 100))
            widget_poi.save()


    def test_attr(self):
        '''
        Test that the attr 'foo' is saved on the widget object.
        '''
        self.assertEqual(self.widget_map['byline'], 'A Nice Map of Nice Points of Interest')

    def test_widget_map_pois_ctype(self):
        '''
        Test that the pois property only returns the right aspects.
        '''
        polymorphic_ctype=ContentType.objects.get_for_model(models.WidgetMapPOI)
        for poi in self.widget_map.pois:
            self.assertEqual(poi.polymorphic_ctype, polymorphic_ctype)

    def tearDown(self):
        Attribute.objects.all().delete()
        models.Widget.objects.all().delete()
