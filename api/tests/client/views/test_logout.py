import json

import pytest
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED

from tests.client.factories.ecommerce_client import EcommerceClientPredictableLoginFactory


@pytest.mark.django_db
class TestLogin:

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
        self.ecommerce_client = EcommerceClientPredictableLoginFactory.create()

    def _get_auth_token(self, api_client):
        response = api_client.post(self._login_url, data={"email": 'test123456789@example.com',
                                                          "password": 'testing_password123'})

        json_response = json.loads(response.content)

        return json_response["token"]


    def test_logout_ok(self, api_client):
        token = self._get_auth_token(api_client)

        response = api_client.post(self.url, headers={'Authorization': f'Token {token}'})

        assert response.status_code == HTTP_204_NO_CONTENT

    def test_logout_no_token(self, api_client):
        response = api_client.post(self.url, headers={})

        assert response.status_code == HTTP_401_UNAUTHORIZED
