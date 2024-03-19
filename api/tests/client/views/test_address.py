import copy
from typing import NoReturn

import pytest
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from rest_framework.test import APIClient

from tests.client.factories.address import AddressFactory
from tests.client.factories.ecommerce_client import EcommerceClientWithoutAddressFactory
from tests.client.utils import authorized_test


@pytest.mark.django_db
class TestAddressCreation:
    
    @classmethod
    def setup_class(cls) -> NoReturn:
        """
        Executed once for the class.
        """
        cls.url = reverse("client:address_creation")
        cls._login_url = reverse("client:login")

    def setup_method(self) -> NoReturn:
        """
        Executed once before each test.
        """
        _ = EcommerceClientWithoutAddressFactory()
        self.address = AddressFactory()

    @property
    def _address_data(self) -> dict:
        return {
            "full_name": self.address.full_name,
            "email": self.address.email,
            "phone_number": self.address.phone_number,
            "full_road": self.address.full_road,
            "extra_info": self.address.extra_info,
            "zip_code": self.address.zip_code,
            "city": self.address.city,
            "country": self.address.country
        }

    @authorized_test
    def test_address_creation_ok(self, api_client: APIClient) -> NoReturn:
        response = api_client.post(self.url, data=self._address_data)

        assert response.status_code == HTTP_201_CREATED

    @authorized_test
    def test_address_creation_ko_incomplete_data(self, api_client: APIClient) -> NoReturn:
        incomplete_address_data = copy.deepcopy(self._address_data)
        incomplete_address_data.pop('city')
        response = api_client.post(self.url, data=incomplete_address_data)

        assert response.status_code == HTTP_400_BAD_REQUEST

    def test_address_creation_ko_unauthorized(self, api_client: APIClient) -> NoReturn:
        response = api_client.post(self.url, data=self._address_data)

        assert response.status_code == HTTP_401_UNAUTHORIZED
