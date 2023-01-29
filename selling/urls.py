from django.urls import re_path

from selling.views.product.list_create import ProductsViewSet
from selling.views.product.retrieve_update_destroy import ProductViewSet

urlpatterns = [
    re_path(r'^products/$', ProductsViewSet.as_view(), name="list_create"),
    re_path(r'^products/(?P<product_id>[0-9_a-zA-Z\-]+)/?$', ProductViewSet.as_view(), name="retrieve_update"),
]
