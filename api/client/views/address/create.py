from knox.auth import TokenAuthentication
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from client.models.ecommerce_client import EcommerceClient
from client.serializers.address import AddressSerializer


class AddressCreationView(CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = AddressSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        client = get_object_or_404(EcommerceClient.objects.all(), id=self.request.user.id)

        if client.address:
            raise ValidationError('This user already has an address.')

        address = serializer.save()
        client.address = address
        client.save()

        return Response(self.get_serializer(address).data, status=status.HTTP_201_CREATED)
