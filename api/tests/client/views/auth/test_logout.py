import json

import pytest
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED

from tests.client.factories.ecommerce_client import EcommerceClientPredictableLoginFactory
from tests.client.utils import authorized_test


@pytest.mark.django_db
class TestLogout:

    @classmethod
    def setup_class(cls):
        """
        Executed once for the class.
        """
        cls.url = reverse("client:knox_logout")
        cls._login_url = reverse("client:login")

    def setup_method(self):
        """
        Executed once before each test.
        """
        self.ecommerce_client = EcommerceClientPredictableLoginFactory()

    @authorized_test
    def test_logout_ok(self, api_client):
        response = api_client.post(self.url)

        assert response.status_code == HTTP_204_NO_CONTENT

    def test_logout_ko_no_token(self, api_client):
        response = api_client.post(self.url, headers={})

        assert response.status_code == HTTP_401_UNAUTHORIZED
