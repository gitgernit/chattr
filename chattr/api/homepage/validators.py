__all__ = []

import django.utils.deconstruct
import rest_framework.exceptions


@django.utils.deconstruct.deconstructible()
class MaxUsersValidator:
    def __init__(self, max_users):
        self.max_users = max_users

    def __call__(self, value):
        if value < 0:
            raise rest_framework.exceptions.ValidationError(
                'Max users must be greater than 0',
            )

        if value >= self.max_users:
            raise rest_framework.exceptions.ValidationError(
                f'Max users must be less than or equal to {self.max_users}',
            )

    def __eq__(self, other):
        return self.max_users == other.max_users


@django.utils.deconstruct.deconstructible()
class MaxIdleTimeValidator:
    def __init__(self, max_idle_time):
        self.max_idle_time = max_idle_time

    def __call__(self, value):
        if value < 0:
            raise rest_framework.exceptions.ValidationError(
                'Max idle time must be greater than 0',
            )

        if value >= self.max_idle_time:
            raise rest_framework.exceptions.ValidationError(
                f'Max idle time must be less than or '
                f'equal to {self.max_idle_time}',
            )

    def __eq__(self, other):
        return self.max_idle_time == other.max_idle_time
