from django.urls import re_path, path, include

from client.views.auth.login import LoginView
from client.views.client.list_create import ClientsViewSet
from client.views.client.retrieve_update_destroy import EcommerceClientViewSet

urlpatterns = [
    re_path(r'^clients/$', ClientsViewSet.as_view(), name="list_create"),
    re_path(r'^client/(?P<client_id>[0-9_a-zA-Z\-]+)/?$', EcommerceClientViewSet.as_view(), name="retrieve_update"),
    re_path(r'^auth/login/', LoginView.as_view(), name="retrieve_update")
]
