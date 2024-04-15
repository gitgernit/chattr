from http import HTTPStatus

import django.core.exceptions
import django.test
from django.test import Client, TestCase
import django.urls


class ApiEndpointsTest(TestCase):
    def test_api_endpoint(self):
        response = django.test.Client().get(f"/api/homepage/get_room/")
        self.assertEqual(response.status_code, HTTPStatus.OK)


__all__ = []
