from knox.models import AuthToken
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from client.models.ecommerce_client import EcommerceClient
from client.serializers.client import EcommerceClientsSerializer, \
    MeSerializer, EcommerceClientCreationSerializer
from common.views import HTTP_CREATE_METHODS


class EcommerceClientsViewSet(ListCreateAPIView):
    queryset = EcommerceClient.objects.all()
    input_serializer_class = EcommerceClientCreationSerializer

    def get_serializer_class(self):
        if self.request.method in HTTP_CREATE_METHODS:
            return MeSerializer
        elif self.request.method == 'GET':
            return EcommerceClientsSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.input_serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        ecommerce_client = serializer.save()
        ecommerce_client.set_password(serializer.validated_data["password"])
        token = AuthToken.objects.create(ecommerce_client)
        ecommerce_client.auth_token = token[1]

        return Response(self.get_serializer(ecommerce_client).data)
