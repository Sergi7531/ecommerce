import json
import random
from typing import NoReturn

import pytest
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK
from rest_framework.test import APIClient

from client.models import EcommerceClient
from tests.client.factories.ecommerce_client import EcommerceClientPredictableLoginFactory
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
                                  data={'username': 'New_username'})
        json_response = json.loads(response.content)

        assert response.status_code == HTTP_200_OK
        assert str(json_response["id"]) == self.ecommerce_client.id
        assert str(json_response["username"]) == 'New_username'

    def test_put_update_client_details_ko_unauthorized(self, api_client: APIClient) -> NoReturn:
        response = api_client.put(self._client_detail_url(self.ecommerce_client.id),
                                  data={'username': 'This_will_not_work'})

        assert response.status_code == HTTP_401_UNAUTHORIZED

    # @authorized_test
    # def test_put_update_client_details_ko_(self):
    #     ...
