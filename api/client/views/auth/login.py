from django.db.models import Q
from django.utils import timezone
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response

from client.managers.knox_auth import KnoxAuthManager
from client.models import EcommerceClient
from client.serializers.auth import LoginSerializer
from client.serializers.client import EcommerceClientSerializer


class LoginView(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def get_object(self):
        email = self.request.data.get('email', None)

        return get_object_or_404(EcommerceClient.objects,
                                 Q(email=email))

    def post(self, request, *args, **kwargs):
        result_status = status.HTTP_200_OK
        result_dict = {}
        auth_serializer = self.get_serializer(data=request.data)
        auth_serializer.is_valid(raise_exception=True)

        client: EcommerceClient = self.get_object()

        if not client.check_password(auth_serializer.validated_data["password"]):
            result_dict["reason"] = "Incorrect email or password"
            result_status = status.HTTP_401_UNAUTHORIZED
        else:
            knox_auth_manager = KnoxAuthManager(request, client)
            result_dict["token"] = knox_auth_manager.knox_login()
            result_dict["client"] = EcommerceClientSerializer(client, many=False).data

        client.last_login = timezone.now()
        client.save()

        return Response(result_dict, status=result_status)
