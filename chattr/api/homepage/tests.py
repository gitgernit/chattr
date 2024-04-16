from http import HTTPStatus

import django.core.exceptions
import django.test
from django.test import TestCase
import django.urls
import parameterized


class ApiEndpointsTest(TestCase):
    def test_api_endpoint(self):
        response = django.test.Client().get('/api/homepage/get_room/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    @parameterized.parameterized.expand(
        [
            (60, 60, HTTPStatus.OK),
            (0, 0, HTTPStatus.OK),
            (-1, 60, HTTPStatus.NOT_FOUND),
            (60, -1, HTTPStatus.NOT_FOUND),
            (-1, -1, HTTPStatus.NOT_FOUND),
            ('asd', 60, HTTPStatus.NOT_FOUND),
            (60, 'asd', HTTPStatus.NOT_FOUND),
            ('dds', 'asd', HTTPStatus.NOT_FOUND),
        ],
    )
    def test_catalog_item_endpoint(self, max_users, max_time, expected_status):
        response = django.test.Client().get(
            '/api/homepage/get_room/'
            f'?max_users={max_users}&max_idle_time={max_time}',
        )
        self.assertEqual(response.status_code, expected_status)


__all__ = []
