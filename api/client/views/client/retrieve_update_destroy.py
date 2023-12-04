from knox.auth import TokenAuthentication
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from client.models import EcommerceClient
from client.serializers.client import MeSerializer, EcommerceClientSerializer
from common.views import HTTP_RETRIEVE_METHODS, HTTP_UPDATE_METHODS


class EcommerceClientViewSet(RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = EcommerceClient.objects.all()
    output_serializer_class = MeSerializer

    def get_serializer_class(self):
        if self.request.method in HTTP_RETRIEVE_METHODS:
            return EcommerceClientSerializer
        elif self.request.method in HTTP_UPDATE_METHODS:
            return EcommerceClientSerializer

    def get_object(self):
        client_id = self.kwargs.get('client_id')
        return get_object_or_404(self.get_queryset(), id=client_id)

    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        client = self.request.user
        password = request.data.get('password')

        # Check for a new password submitted within the update request:
        if password and not client.check_password(password):
            client.set_password(password)

        return Response(self.output_serializer_class(instance).data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        client = self.get_object()
        EcommerceClient.delete(client)

        return Response(self.get_serializer(client).data, status=status.HTTP_200_OK)
