import copy
import json
from typing import NoReturn, Literal

import factory
import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.test import APIClient

from tests.client.factories.ecommerce_client import EcommerceClientFactory


@pytest.mark.django_db
class TestCreateEcommerceClient:

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
        self.ecommerce_client = EcommerceClientFactory.build()

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
        incomplete_ecommerce_data = copy.deepcopy(self._ecommerce_client_creation_data)
        incomplete_ecommerce_data.pop('first_name')

        response = api_client.post(self.url, data=incomplete_ecommerce_data)

        assert response.status_code == HTTP_400_BAD_REQUEST

    def test_ecommerce_client_create_username_in_use(self, api_client: APIClient) -> NoReturn:
        self._test_ecommerce_client_creation_existing_field(api_client, 'username')

    def test_ecommerce_client_create_email_in_use(self, api_client: APIClient) -> NoReturn:
        self._test_ecommerce_client_creation_existing_field(api_client, 'email')

    def _test_ecommerce_client_creation_existing_field(self, api_client: APIClient, field_name: Literal['username', 'email']) -> NoReturn:
        ecommerce_data_copy = copy.deepcopy(self._ecommerce_client_creation_data)

        _ = api_client.post(self.url, data=ecommerce_data_copy)

        ecommerce_data_copy[field_name] = factory.Faker(field_name)

        response = api_client.post(self.url, data=self._ecommerce_client_creation_data)
        json_response = json.loads(response.content)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert any(map(lambda error_msg: f"{field_name} already exists" in error_msg, json_response.get(field_name, "")))
