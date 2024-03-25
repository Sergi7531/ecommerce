from rest_framework.serializers import ModelSerializer

from selling.models.payment_method import PaymentMethod


class PaymentMethodSerializer(ModelSerializer):

    class Meta:
        model = PaymentMethod
        fields = ('id', 'name')