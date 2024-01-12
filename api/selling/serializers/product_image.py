from rest_framework import serializers

from selling.models.product_image import ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('type', 'url')
