import pytest
from rest_framework.reverse import reverse

from tests.client.factories.ecommerce_client import EcommerceClientPredictableFactory


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
        self.ecommerce_client = EcommerceClientPredictableFactory()

    def test_login_ok(self, api_client):
        response = api_client.post(
            path=self.url,
            data={"email": self.ecommerce_client.email,
                  "password": f"{self.ecommerce_client.first_name}.{self.ecommerce_client.last_name}"})

        assert response.status_code == 200
        assert response['token'] is not None
        assert response['id'] == self.ecommerce_client.id

    def test_login_wrong_password(self, api_client):
        response = api_client.post(path=self.url,
                                   data={"email": self.ecommerce_client.email, "password": "incorrect_password"})

        assert response.status_code == 403

    def test_login_inexistent_client_email(self, api_client):
        response = api_client.post(path=self.url, data={"email": f'foo_{self.ecommerce_client.email}',
                                                        "password": "incorrect_password"})

        assert response.status_code == 404
