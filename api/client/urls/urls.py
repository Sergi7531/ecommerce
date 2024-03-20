from django.urls import re_path
from knox import views as knox_views

from client.views.address.create import AddressCreationView
from client.views.auth.login import LoginView
from client.views.client.list_create import EcommerceClientsViewSet
from client.views.client.me import MeView
from client.views.client.retrieve_update_destroy import EcommerceClientViewSet

app_name='client'

urlpatterns = [
    re_path(r'^clients/$', EcommerceClientsViewSet.as_view(), name="ecommerce_client_list_create"),
    re_path(r'^client/(?P<client_id>[0-9_a-zA-Z\-]+)/?$', EcommerceClientViewSet.as_view(), name="retrieve_update"),
    re_path(r'^clients/address/?$', AddressCreationView.as_view(), name="address_creation"),
    re_path(r'^me/$', MeView.as_view(), name="retrieve_me"),
    re_path(r'^login/$', LoginView.as_view(), name="login"),
    re_path(r'^logout/$', knox_views.LogoutView.as_view(), name='knox_logout'),
]
