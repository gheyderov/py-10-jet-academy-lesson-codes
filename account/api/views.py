from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from drf_yasg.utils import swagger_auto_schema
from account.api.serializers import UserAPIDocProfileSerializer


class UserTokenObtainPairView(TokenObtainPairView):

    @swagger_auto_schema(responses={200: UserAPIDocProfileSerializer(many=True)})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)