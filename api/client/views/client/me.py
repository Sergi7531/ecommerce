from knox.auth import TokenAuthentication
from rest_framework.generics import RetrieveAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated

from client.models import EcommerceClient
from client.serializers.client import MeSerializer
from common.views import HTTP_RETRIEVE_METHODS


class MeView(RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = EcommerceClient.objects.all()

    def get_serializer_class(self):
        if self.request.method in HTTP_RETRIEVE_METHODS:
            return MeSerializer

    def get_object(self):
        client_id = self.request.user.id
        return get_object_or_404(self.get_queryset(), id=client_id)
