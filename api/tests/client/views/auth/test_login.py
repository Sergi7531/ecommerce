import json
from uuid import UUID

import pytest
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK, HTTP_404_NOT_FOUND

from tests.client.factories.ecommerce_client import EcommerceClientPredictableLoginFactory


@pytest.mark.django_db
class TestLogin:

    @classmethod
    def setup_class(cls):
        """
        Executed once for the class.
        """
        cls.url = reverse("client:login")

    def setup_method(self):
        """
        Executed once before each test.
        """
        self.ecommerce_client = EcommerceClientPredictableLoginFactory()

    def test_login_ok(self, api_client):
        response = api_client.post(path=self.url, data={"email": 'test123456789@example.com',
                                                        "password": 'testing_password123'})

        json_response = json.loads(response.content)

        assert response.status_code == HTTP_200_OK
        assert json_response['token'] is not None
        assert UUID(json_response['client']['id']) == self.ecommerce_client.id

    def test_login_wrong_password(self, api_client):
        response = api_client.post(path=self.url,
                                   data={"email": 'test123456789@example.com', "password": "incorrect_password"})

        assert response.status_code == HTTP_403_FORBIDDEN

    def test_login_inexistent_client_email(self, api_client):
        response = api_client.post(path=self.url, data={"email": f'inexistent_email@wrong.com',
                                                        "password": "testing_password123"})

        assert response.status_code == HTTP_404_NOT_FOUND
