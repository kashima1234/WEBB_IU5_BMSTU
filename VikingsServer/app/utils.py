import random
from datetime import datetime, timedelta
from django.utils import timezone

from rest_framework import serializers


class CustomSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):

        excluded_fields = kwargs.pop('excluded_fields', None)

        super().__init__(*args, **kwargs)

        if excluded_fields is not None:
            excluded = set(excluded_fields)
            for field_name in excluded:
                self.fields.pop(field_name)


def random_date():
    now = datetime.now(tz=timezone.utc)
    return now + timedelta(random.uniform(-1, 0) * 100)


def random_timedelta(factor=100):
    return timedelta(random.uniform(0, 1) * factor)


def random_bool():
    return bool(random.getrandbits(1))
