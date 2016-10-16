import json

from rest_framework import (
    parsers,
    permissions,
    renderers,
    status,
    views,
    viewsets,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.utils import jwt_response_payload_handler
from rest_framework_jwt.serializers import JSONWebTokenSerializer


from .models import User
from .serializers import UserSerializer
from .permissions import IsOwnAccount


class UserViewSet(viewsets.ModelViewSet):
    """User API Views"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsOwnAccount(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            User.objects.create(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'Bad request',
            'message': 'User could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """User login view"""
    parser_classes = (parsers.FormParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = JSONWebTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(token, user, request)

            return Response(response_data)

        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
