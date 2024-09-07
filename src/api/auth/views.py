from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from src.apps.user.serializers import UserSerializer


class RegisterUser(CreateAPIView):
    """View для регистрации пользователя"""

    def post(self, request, **kwargs):
        if request.method == "POST":
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
