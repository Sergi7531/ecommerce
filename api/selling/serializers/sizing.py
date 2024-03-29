from rest_framework.serializers import ModelSerializer

from selling.models.sizing import Sizing


class SizingSerializer(ModelSerializer):
    class Meta:
        model = Sizing
        fields = ('id', 'size_type', 'amount', 'size_short')
