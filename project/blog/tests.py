"""
Run "./manage.py test blog" from healthblog root.
"""
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from .models import *
import datetime # need to make timezone aware
import urllib.parse

class AuthorizationTests(TestCase):

    def setUp(self):
        # To fully test, create poster accounts here, and check that they can do things
        # In the interests of brevity, just testing redirect to login if not logged in
        pass

    def testNoAccessWithoutLogin(self):
        """
        Tests that redirected to the home/login page if you are not logged in
        """
        response = self.client.get(reverse('questionList'), follow=True)
        expected_url = reverse('home') + "?next=" + reverse('questionList')
        self.assertRedirects(response, expected_url, status_code=302, 
            target_status_code=200)
        expected_url = reverse('home') + "?next=" + reverse('questionAdd')
        response = self.client.get(reverse('questionAdd'), follow=True)
        self.assertRedirects(response, expected_url, status_code=302, 
            target_status_code=200)