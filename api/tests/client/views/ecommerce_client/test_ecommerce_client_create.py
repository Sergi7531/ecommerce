import copy
from typing import NoReturn

import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.test import APIClient

from tests.client.factories.ecommerce_client import EcommerceClientFactory


@pytest.mark.django_db
class TestEcommerceClient:

    @classmethod
    def setup_class(cls) -> NoReturn:
        """
        Executed once for the class.
        """
        cls.url = reverse("client:ecommerce_client_list_create")

    def setup_method(self) -> NoReturn:
        """
        Executed once before each test.
        """
        self.ecommerce_client = EcommerceClientFactory()

    @property
    def _ecommerce_client_creation_data(self) -> dict:
        return {
            "id": self.ecommerce_client.id,
            "username": self.ecommerce_client.username,
            "first_name": self.ecommerce_client.first_name,
            "last_name": self.ecommerce_client.last_name,
            "email": self.ecommerce_client.email,
            "password": self.ecommerce_client.password
        }

    def test_ecommerce_client_create_ok(self, api_client: APIClient) -> NoReturn:
        response = api_client.post(self.url, data=self._ecommerce_client_creation_data)

        assert response.status_code == status.HTTP_201_CREATED

    def test_ecommerce_client_create_incomplete_data(self, api_client: APIClient) -> NoReturn:
        incomplete_address_data = copy.deepcopy(self._ecommerce_client_creation_data)
        incomplete_address_data.pop('first_name')

        response = api_client.post(self.url, data=self._ecommerce_client_creation_data)

        assert response.status_code == HTTP_400_BAD_REQUEST

    def test_ecommerce_client_create_email_in_use(self, api_client: APIClient) -> NoReturn:
        response = api_client.post(self.url, data=self._ecommerce_client_creation_data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
