from knox.auth import TokenAuthentication
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class CheckoutViewSet(RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        """
        The view must create an order:

        The order will have:
        - A link to the shopping cart (to have a snapshot of the ordered products)
        - An address
        - A payment method
        - A discount code (optional)
        - A shipping "option" (Standard shipping: 5€, or free with an order of 50€ or higher. "Premium" shipping: 10€)
        """

        return Response(status=HTTP_200_OK)
