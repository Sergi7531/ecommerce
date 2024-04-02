import json
from typing import NoReturn

import pytest
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework.test import APIClient

from tests.client.factories.ecommerce_client import EcommerceClientPredictableLoginFactory
from tests.client.utils import authorized_test
from tests.conftest import load_payment_methods


@pytest.mark.django_db
class TestPaymentMethodsList:

    @classmethod
    def setup_class(cls) -> NoReturn:
        """
        Executed once for the class.
        """
        cls.url = reverse("selling:payment_methods_list")
        cls._login_url = reverse("client:login")

    def setup_method(self) -> NoReturn:
        """
        Executed once before each test.
        """
        self.ecommerce_client = EcommerceClientPredictableLoginFactory()

    @authorized_test
    def test_payment_methods_list(self, api_client: APIClient, load_payment_methods: None) -> NoReturn:
        response = api_client.get(self.url)
        json_response = json.loads(response.content)

        assert response.status_code == HTTP_200_OK
        assert len(json_response) > 0

    def test_payment_methods_ko_unauthorized(self, api_client: APIClient) -> NoReturn:
        response = api_client.get(self.url)

        assert response.status_code == HTTP_401_UNAUTHORIZED
