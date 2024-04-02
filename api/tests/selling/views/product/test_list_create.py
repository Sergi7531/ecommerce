import json
from typing import NoReturn

import pytest
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework.test import APIClient

from tests.client.factories.ecommerce_client import EcommerceClientPredictableLoginFactory
from tests.client.utils import authorized_test
from tests.selling.factories.product_factory import ProductFactory


@pytest.mark.django_db
class TestListCreateEcommerceClient:

    @classmethod
    def setup_class(cls) -> NoReturn:
        """
        Executed once for the class.
        """
        cls.url = reverse("selling:product_list_create")
        cls._login_url = reverse("client:login")

    def setup_method(self) -> NoReturn:
        """
        Executed once before each test.
        """
        self.ecommerce_client = EcommerceClientPredictableLoginFactory()
        self.test_product = ProductFactory(name="Test Product", price=9999)

    @authorized_test
    def test_list_products_ok(self, api_client: APIClient) -> NoReturn:
        response = api_client.get(self.url)
        json_response = json.loads(response.content)

        assert response.status_code == HTTP_200_OK
        assert any(str(self.test_product.id) == str(product.get("id", "")) for product in json_response)

    def test_list_products_filter(self, api_client: APIClient) -> NoReturn:
        response = api_client.get(f"{self.url}?name=Test Product")
        json_response = json.loads(response.content)

        assert len(json_response) >= 1

        response = api_client.get(f"{self.url}?min_price=9999")
        json_response = json.loads(response.content)

        assert len(json_response) >= 1

        response = api_client.get(f"{self.url}?max_price=9999")
        json_response = json.loads(response.content)

        assert len(json_response) >= 1

    def test_new_produçt_ok(self, api_client: APIClient) -> NoReturn:
        # response = api_client.post(self.url, data=self.test_product.__dict__)
        pass