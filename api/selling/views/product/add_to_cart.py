from knox.auth import TokenAuthentication
from rest_framework import status
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from selling.models import Product
from selling.models.shopping_cart_product import ShoppingCartProduct
from selling.models.sizing import Sizing
from selling.serializers.shopping_cart import AddToCartSerializer, ShoppingCartSerializer


class AddToCartView(CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = AddToCartSerializer
    output_serializer_class = ShoppingCartSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.request.user
        cart = user.shopping_cart

        product = get_object_or_404(Product, id=serializer.validated_data['product_id'])
        sizing = get_object_or_404(Sizing.objects.filter(product_id=product.id), id=serializer.validated_data['sizing_id'])

        cart.add_product_to_cart(product, sizing, serializer.validated_data['amount'])

        return Response(self.output_serializer_class(cart).data, status=status.HTTP_201_CREATED)
