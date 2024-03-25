import json
import random
from typing import NoReturn

import pytest
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK, HTTP_403_FORBIDDEN
from rest_framework.test import APIClient

from client.models import EcommerceClient
from tests.client.factories.ecommerce_client import EcommerceClientPredictableLoginFactory, EcommerceClientFactory
from tests.client.utils import authorized_test


@pytest.mark.django_db
class TestRetrieveUpdate:

    @classmethod
    def setup_class(cls) -> NoReturn:
        """
        Executed once for the class.
        """
        cls._reversed_retrieve_update_url = "client:ecommerce_client_retrieve_update"
        cls._login_url = reverse("client:login")

    def setup_method(self) -> NoReturn:
        """
        Executed once before each test.
        """
        self.ecommerce_client = EcommerceClientPredictableLoginFactory()

    def _client_detail_url(self, client_id: str) -> str:
        # Used in runtime to dynamically reverse the _reversed_retrieve_update_url
        return reverse(self._reversed_retrieve_update_url, args=[client_id])

    @property
    def _update_data(self):
        return {"username": "New_username",
                "first_name": "New_first_name",
                "last_name": "New_last_name",
                "address": {
                    "id": self.ecommerce_client.address.id,
                    "full_name": self.ecommerce_client.address.full_name,
                    "email": self.ecommerce_client.address.email,
                    "phone_number": self.ecommerce_client.address.phone_number,
                    "full_road": self.ecommerce_client.address.full_road,
                    "extra_info": self.ecommerce_client.address.extra_info,
                    "zip_code": self.ecommerce_client.address.zip_code,
                    "city": self.ecommerce_client.address.city,
                    "country": self.ecommerce_client.address.country
                }
                }

    @authorized_test
    def test_get_public_client_details_ok(self, api_client: APIClient) -> NoReturn:
        random_client = random.choice(EcommerceClient.objects.all())
        response = api_client.get(self._client_detail_url(random_client.id))
        json_response = json.loads(response.content)

        assert response.status_code == HTTP_200_OK
        assert json_response["id"] == str(random_client.id)

    def test_get_public_client_details_ko_unauthorized(self, api_client: APIClient) -> NoReturn:
        random_client = random.choice(EcommerceClient.objects.all())

        response = api_client.get(self._client_detail_url(random_client.id))

        assert response.status_code == HTTP_401_UNAUTHORIZED

    @authorized_test
    def test_put_update_client_details_ok(self, api_client: APIClient) -> NoReturn:
        response = api_client.put(self._client_detail_url(self.ecommerce_client.id),
                                  data=self._update_data, format="json")
        json_response = json.loads(response.content)

        assert response.status_code == HTTP_200_OK
        assert json_response["id"] == str(self.ecommerce_client.id)
        assert json_response["username"] == "New_username"

    def test_put_update_client_details_ko_unauthorized(self, api_client: APIClient) -> NoReturn:
        response = api_client.put(self._client_detail_url(self.ecommerce_client.id),
                                  data=self._update_data, format="json")

        assert response.status_code == HTTP_401_UNAUTHORIZED

    @authorized_test
    def test_put_update_client_details_ko_invalid_token_for_provided_uuid(self, api_client: APIClient) -> NoReturn:
        new_random_client = EcommerceClientFactory()

        response = api_client.put(self._client_detail_url(new_random_client.id),
                                  data={"username": "This_will_not_work"})

        assert response.status_code == HTTP_403_FORBIDDEN
