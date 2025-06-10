from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import authenticate
from rest_framework.authtoken.models import Token

from . import models
from . import serializer


@api_view(["POST"])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")

    if not email or not password:
        return Response({"error": {'message': "Validation error", 'code': 422}})

    user = authenticate(email=email, password=password)

    if not user:
        return Response({'error': {'message': "Authentication failed", 'code': 401}})

    token, _ = Token.objects.get_or_create(user=user)

    return Response({'data': {'user_token': token.key}})


@api_view(['POST'])
def signup(request):
    serialize_data = serializer.UserSerializer(data=request.data)
    if serialize_data.is_valid():
        user = serialize_data.save()
        token, _ = Token.objects.get_or_create(user=user)

        return Response({'data': {'user_token': token.key, 'code': 201}})
    return Response({'error': serialize_data.errors})


@api_view(["GET"])
def logout(request):
    request.user.auth_token.delete()

    return Response({'data': {'message': 'logout', 'code': 200}})
