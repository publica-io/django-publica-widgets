# -*- coding: utf-8 -*-
from django.test import TestCase

from .models import Widget, WidgetMailChimpSignup


class WidgetsTestCase(TestCase):
    def setUp(self):
        widget = Widget.objects.create(
            title='This is my long widget title',
            short_title='A neat short title',
            text='some nice neat long text that should be tested for good',
            slug='this-is-my-long-widget-title'
        )
        WidgetMailChimpSignup.objects.create(
            widget=widget,
            list_name='here should be a long string for the widget mail signup'
        )

    def test_widget_title(self):
        widget = Widget.objects.get(slug='this-is-my-long-widget-title')
        self.assertEqual(widget.title, 'This is my long widget title')

    def test_widget_short_title(self):
        widget = Widget.objects.get(slug='this-is-my-long-widget-title')
        self.assertEqual(widget.short_title, 'A neat short title')

    def test_widget_text(self):
        widget = Widget.objects.get(slug='this-is-my-long-widget-title')
        self.assertEqual(
            widget.text,
            'some nice neat long text that should be tested for good'
        )

    def test_widget_slug(self):
        widget = Widget.objects.get(slug='this-is-my-long-widget-title')
        self.assertEqual(widget.slug, 'this-is-my-long-widget-title')

    def test_widget_mailchimp_signup_widget(self):
        widget = Widget.objects.get(slug='this-is-my-long-widget-title')
        widget_mailchimp_signup = WidgetMailChimpSignup.objects.get(
            list_name='here should be a long string for the widget mail signup'
        )
        self.assertEqual(widget_mailchimp_signup.widget, widget)

    def test_widget_mailchimp_signup_list_name(self):
        widget_mailchimp_signup = WidgetMailChimpSignup.objects.get(
            list_name='here should be a long string for the widget mail signup'
        )
        self.assertEqual(
            widget_mailchimp_signup.list_name,
            'here should be a long string for the widget mail signup'
        )
