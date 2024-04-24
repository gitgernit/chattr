import http

import django.test
import django.urls

__all__ = []


class HomepageStaticURLTests(django.test.TestCase):
    def test_homepage_endpoint(self):
        response = self.client.get(django.urls.reverse('room:room'))
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
