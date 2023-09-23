from django.urls import re_path

from selling.views.product.list_create import ProductsViewSet
from selling.views.product.retrieve_update_destroy import ProductViewSet
from selling.views.shopping_cart import ShoppingCartViewSet
from selling.views.tags.list_create import TagsViewSet
from selling.views.tags.retrieve_update_destroy import TagViewSet

urlpatterns = [
    # Products:
    re_path(r'^products/$', ProductsViewSet.as_view(), name="list_create"),
    re_path(r'^products/(?P<product_id>[0-9_a-zA-Z\-]+)/?$', ProductViewSet.as_view(), name="retrieve_update"),

    # Tags:
    re_path(r'^tags/$', TagsViewSet.as_view(), name="list_create"),
    re_path(r'^tags/(?P<tag_id>[0-9]+)/?$', TagViewSet.as_view(), name="retrieve_update_destroy"),

    # Shopping cart:
    re_path(r'^shopping_cart/(?P<shopping_cart_id>[0-9]+)/?$', ShoppingCartViewSet.as_view(), name="retrieve_update"),
]
