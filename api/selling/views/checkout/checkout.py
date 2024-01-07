from knox.auth import TokenAuthentication
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from selling.serializers.order import OrderInputSerializer, OrderOutputSerializer


class CheckoutView(CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderInputSerializer
    output_serializer_class = OrderOutputSerializer

    """
    The view will create an order:

    The order will have:
    - A link to the shopping cart (to have a snapshot of the ordered products)
    - An address
    - A payment method
    - A discount code (optional)
    - A shipping "option" (Standard shipping: 5€, or free with an order of 50€ or higher. "Premium" shipping: 10€)
    """

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()

        return Response(self.output_serializer_class(order).data, status=status.HTTP_201_CREATED)

