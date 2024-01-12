from knox.auth import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from selling.models import PaymentMethod
from selling.serializers.payment_method import PaymentMethodSerializer


class PaymentMethodsView(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = PaymentMethodSerializer
    queryset = PaymentMethod.objects.all()