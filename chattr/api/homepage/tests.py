from http import HTTPStatus

import django.core.exceptions
import django.test
from django.test import Client, TestCase
import django.urls
import parameterized


class ApiEndpointsTest(TestCase):
    @parameterized.parameterized.expand(
        [
            ("1", HTTPStatus.OK),
        ],
    )
    def test_api_endpoint(self, url, expected_status):
        response = Client().get(django.urls.reverse("api_homepage:get_room"))
        self.assertEqual(response.status_code, expected_status)


__all__ = []
