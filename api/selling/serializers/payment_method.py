from rest_framework.serializers import ModelSerializer

from selling.models import PaymentMethod


class PaymentMethodSerializer(ModelSerializer):

    class Meta:
        model = PaymentMethod
        fields = ('id', 'name')