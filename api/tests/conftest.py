import pytest
from django.core.management import call_command
from rest_framework.test import APIClient


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()

@pytest.fixture(scope="function")
def load_payment_methods(db, django_db_setup, django_db_blocker) -> None:
    call_command("loaddata", "selling/fixtures/payment_methods/payment_method.json")
