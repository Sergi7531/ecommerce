from django.db.models import Q
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response

from client.models import EcommerceClient
from client.serializers.auth import LogoutSerializer


class LogoutView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LogoutSerializer

    def get_object(self):
        user_id = self.request.data.get('user_id')

        return get_object_or_404(EcommerceClient.objects, Q(id=user_id))

    def post(self, request, *args, **kwargs):
        status_code = status.HTTP_200_OK
        result_dict = {}
        auth_serializer = self.get_serializer(data=request.data)
        auth_serializer.is_valid(raise_exception=True)

        client: EcommerceClient = self.get_object()

        if not client.has_token(request.auth_token):
            result_dict["reason"] = "Token to remove isn't owned by logged user. Try logging out and in."
            status_code = status.HTTP_403_FORBIDDEN
        else:
            client.remove_token(request.auth_token)
            result_dict["message"] = "Token removed"

        return Response(result_dict, status_code)
