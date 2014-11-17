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

from widgets import models


class TestWidgets(unittest.TestCase):

    def setUp(self):
        
        self.widget = models.Widget(
            title = 'foo',
            slug = 'foo')
        self.widget.save()
        self.widget['foo'] = 'bar'


    def test_attr(self):
        self.assertEqual(self.widget['foo'], 'bar')


    def tearDown(self):
        pass
