__all__ = []

import http

import django.test
import django.urls


class HomepageStaticURLTests(django.test.TestCase):
    def test_homepage_endpoint(self):
        response = self.client.get(django.urls.reverse('homepage:homepage'))
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
