import json
from typing import NoReturn
from uuid import UUID

import pytest
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.test import APIClient

from tests.client.factories.ecommerce_client import EcommerceClientPredictableLoginFactory
from tests.client.utils import authorized_test


@pytest.mark.django_db
class TestMe:

    @classmethod
    def setup_class(cls) -> NoReturn:
        """
        Executed once for the class.
        """
        cls.url = reverse("client:retrieve_me")
        cls._login_url = reverse("client:login")

    def setup_method(self) -> NoReturn:
        """
        Executed once before each test.
        """
        self.ecommerce_client = EcommerceClientPredictableLoginFactory()

    @authorized_test
    def test_me(self, api_client: APIClient) -> NoReturn:
        response = api_client.get(self.url)

        json_response = json.loads(response.content)

        if json_response["address"] is not None:
            assert UUID(json_response["address"]["id"]) == self.ecommerce_client.address.id

        assert UUID(json_response["id"]) == self.ecommerce_client.id

    def test_me_unauthorized(self, api_client: APIClient) -> NoReturn:
        response = api_client.get(self.url)

        assert response.status_code == HTTP_401_UNAUTHORIZED