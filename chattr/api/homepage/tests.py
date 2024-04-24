__all__ = []

import http

import django.test
import django.urls
import parameterized
import rest_framework.reverse


class ApiEndpointsTest(django.test.TestCase):
    def test_api_endpoint(self):
        response = self.client.get(
            rest_framework.reverse.reverse('api:api_homepage:get_room'),
        )
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    @parameterized.parameterized.expand(
        [
            (60, 60, http.HTTPStatus.OK),
            (0, 0, http.HTTPStatus.OK),
            (-1, 60, http.HTTPStatus.BAD_REQUEST),
            (60, -1, http.HTTPStatus.BAD_REQUEST),
            (-1, -1, http.HTTPStatus.BAD_REQUEST),
            ('asd', 60, http.HTTPStatus.BAD_REQUEST),
            (60, 'asd', http.HTTPStatus.BAD_REQUEST),
            ('dds', 'asd', http.HTTPStatus.BAD_REQUEST),
        ],
    )
    def test_catalog_item_endpoint(self, max_users, max_time, expected_status):
        response = self.client.get(
            rest_framework.reverse.reverse('api:api_homepage:get_room')
            + f'?max_users={max_users}'
            + f'&max_idle_time={max_time}',
        )
        self.assertEqual(response.status_code, expected_status)
