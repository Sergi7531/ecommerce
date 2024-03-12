import pytest


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()

# @pytest.fixture(scope="session")
# def django_db_setup(django_db_setup, django_db_blocker):
#     pass

# with django_db_blocker.unblock():
#     ContentType.objects.all().delete()
# AUTH
# call_command("loaddata", "core/fixtures/content_type.json")
