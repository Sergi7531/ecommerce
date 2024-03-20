import json
from functools import wraps
from typing import Optional


def authorized_test(func, email: Optional[str] = None, password: Optional[str] = None):
    @wraps(func)
    def wrapper(self, api_client, *args, **kwargs):
        _email = email or 'test123456789@example.com'
        _password = password or 'testing_password123'
        response = api_client.post(self._login_url, data={"email": _email, "password": _password})

        api_client.credentials(HTTP_AUTHORIZATION=f'Token {json.loads(response.content)["token"]}')
        return func(self, api_client, *args, **kwargs)
    return wrapper
