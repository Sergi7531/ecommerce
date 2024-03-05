import pytest
from django.contrib.contenttypes.models import ContentType
from django.core.management import call_command
from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        ContentType.objects.all().delete()

        # AUTH
        # call_command("loaddata", "core/fixtures/content_type.json")
