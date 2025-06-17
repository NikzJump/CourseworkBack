from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import authenticate
from rest_framework.authtoken.models import Token

from .models import product_models, user_models
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


@api_view(["GET"])
def get_products(request):
    products = product_models.Products.objects.all()
    serialize_data = serializer.ProductsSerializer(products, many=True)

    return Response({"data": serialize_data.data, "code": 200})


@api_view(["GET"])
def get_cart(request):
    if not request.user.is_active:
        return Response({'“error”: {“code”: 403,“message”: “Forbidden for you”}'})

    cart, _ = user_models.Cart.objects.get_or_create(user=request.user)
    serialize_data = serializer.CartSerializer(cart)
    data = []
    cnt = 0

    for cart_product in serialize_data.data['products']:
        cnt += 1
        data.append({
            "id": cnt,
            "product_id": cart_product["id"],
            "title": cart_product["title"],
            "description": cart_product["description"],
            "price": cart_product["price"],
        })
