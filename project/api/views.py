# Обработка всех запросов с последующим отправлением ответов на фронт

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import authenticate
from rest_framework.authtoken.models import Token

from . import serializer, models


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


# Исправить эту дичь отдельной моделькой
@api_view(["GET"])
def get_products(request):
    processors = models.Processor.objects.all()
    graphic_cards = models.GraphicCard.objects.all()
    motherboards = models.Motherboard.objects.all()
    RAM = models.RAM.objects.all()
    discs = models.Disc.objects.all()
    coolers = models.Cooler.objects.all()
    cases = models.Case.objects.all()
    power_unit = models.PowerUnit.objects.all()
    fans = models.Fan.objects.all()
    monitors = models.Monitor.objects.all()
    keyboards = models.Keyboard.objects.all()
    mouses = models.Mouse.objects.all()
    headphones = models.Headphones.objects.all()

    serialize_processors = serializer.ProcessorProdSerializer(processors, many=True)
    serialize_graphic_cards = serializer.GraphicCardProdSerializer(graphic_cards, many=True)
    serialize_motherboards = serializer.MotherboardProdSerializer(motherboards, many=True)
    serialize_RAM = serializer.RAMProdSerializer(RAM, many=True)
    serialize_discs = serializer.DiscProdSerializer(discs, many=True)
    serialize_coolers = serializer.CoolerProdSerializer(coolers, many=True)
    serialize_cases = serializer.CaseProdSerializer(cases, many=True)
    serialize_power_units = serializer.PowerUnitProdSerializer(power_unit, many=True)
    serialize_fans = serializer.FanProdSerializer(fans, many=True)
    serialize_monitors = serializer.MonitorProdSerializer(monitors, many=True)
    serialize_keyboards = serializer.KeyboardProdSerializer(keyboards, many=True)
    serialize_mouses = serializer.MouseProdSerializer(mouses, many=True)
    serialize_headphones = serializer.HeadphonesProdSerializer(headphones, many=True)

    return Response({
        "data": [
            serialize_RAM.data,
            serialize_mouses.data,
            serialize_fans.data,
            serialize_cases.data,
            serialize_discs.data,
            serialize_coolers.data,
            serialize_monitors.data,
            serialize_headphones.data,
            serialize_monitors.data,
            serialize_keyboards.data,
            serialize_motherboards.data,
            serialize_graphic_cards.data,
            serialize_power_units.data,
            serialize_processors.data,
        ],
        "code": 200
    })


# Исправить этот ужас
@api_view(['POST', 'DELETE'])
def add_cart(request, pk, category_id):
    if not request.user.is_active:
        return Response({"error": {"code": 403, "message": "Forbidden for you"}})

    product = None
    cart, _ = models.Cart.objects.get_or_create(user=request.user)

    match category_id:
        case 1:
            product = models.Processor.objects.get(pk=pk)
        case 2:
            product = models.Motherboard.objects.get(pk=pk)
        case 3:
            product = models.RAM.objects.get(pk=pk)
        case 4:
            product = models.GraphicCard.objects.get(pk=pk)
        case 5:
            product = models.Disc.objects.get(pk=pk)
        case 6:
            product = models.Cooler.objects.get(pk=pk)
        case 7:
            product = models.Case.objects.get(pk=pk)
        case 8:
            product = models.PowerUnit.objects.get(pk=pk)
        case 9:
            product = models.Fan.objects.get(pk=pk)
        case 10:
            product = models.Monitor.objects.get(pk=pk)
        case 11:
            product = models.Keyboard.objects.get(pk=pk)
        case 12:
            product = models.Mouse.objects.get(pk=pk)
        case 13:
            product = models.Headphones.objects.get(pk=pk)

    if request.method == 'POST':
        match category_id:
            case 1:
                cart.processors.add(product)
            case 2:
                cart.motherboards.add(product)
            case 3:
                cart.RAM.add(product)
            case 4:
                cart.graphic_cards.add(product)
            case 5:
                cart.discs.add(product)
            case 6:
                cart.coolers.add(product)
            case 7:
                cart.cases.add(product)
            case 8:
                cart.power_unit.add(product)
            case 9:
                cart.fan.add(product)
            case 10:
                cart.monitor.add(product)
            case 11:
                cart.keyboard.add(product)
            case 12:
                cart.mouse.add(product)
            case 13:
                cart.headphones.add(product)
        return Response({'message': 'product added to cart', "code": 201})

    elif request.method == 'DELETE':
        match category_id:
            case 1:
                cart.processors.remove(product)
            case 2:
                cart.motherboards.remove(product)
            case 3:
                cart.RAM.remove(product)
            case 4:
                cart.graphic_cards.remove(product)
            case 5:
                cart.discs.remove(product)
            case 6:
                cart.coolers.remove(product)
            case 7:
                cart.cases.remove(product)
            case 8:
                cart.power_unit.remove(product)
            case 9:
                cart.fan.remove(product)
            case 10:
                cart.monitor.remove(product)
            case 11:
                cart.keyboard.remove(product)
            case 12:
                cart.mouse.remove(product)
            case 13:
                cart.headphones.remove(product)

        return Response({'message': 'product removed from cart', "code": 200})


@api_view(["GET"])
def get_cart(request):
    if not request.user.is_active:
        return Response({"error": {"code": 403, "message": "Forbidden for you"}})

    cart, _ = models.Cart.objects.get_or_create(user=request.user)
    serialize_data = serializer.CartSerializer(cart)
    categories = [
        "processors", "graphic_cards", "motherboards", "RAM", "discs", "coolers",
        "cases", "power_unit", "fan", "monitor", "keyboard", "mouse", "headphones"
    ]

    data = []

    for category in categories:
        for cart_product in serialize_data.data[f'{category}']:
            data.append({
                "product_id": cart_product["id"],
                "title": cart_product["title"],
                "description": cart_product["description"],
                "price": cart_product["price"],
                "category": category
            })

    return Response({"data": data, "code": 200})


@api_view(["GET", "POST"])
def get_order(request):
    if not request.user.is_active:
        return Response({"error": {"code": 403, "message": "Forbidden for you"}})

    orders = models.Order.objects.filter(user=request.user)
    serialize_data = serializer.OrderSerializer(orders, many=True)
    categories = [
        "processors", "graphic_cards", "motherboards", "RAM", "discs", "coolers",
        "cases", "power_unit", "fan", "monitor", "keyboard", "mouse", "headphones"
    ]

    if request.method == "GET":
        data = []
        order_price = 0
        for category in categories:
            for order in serialize_data.data:
                for product_data in order[f"{category}"]:
                    order_price += product_data["price"]
                    data.append({
                        "product_id": product_data["id"],
                        "title": product_data["title"],
                        "description": product_data["description"],
                        "price": product_data["price"],
                        "category": category,
                        "order_price": order_price
                    })

        return Response({"data": data, "code": 200})
    elif request.method == "POST":
        order = models.Order.objects.create(user=request.user)
        cart, _ = models.Cart.objects.get_or_create(user=request.user)

        for product in cart.processors.all():
            order.processors.add(product)

        for product in cart.discs.all():
            order.discs.add(product)

        for product in cart.monitor.all():
            order.monitor.add(product)

        for product in cart.coolers.all():
            order.coolers.add(product)

        for product in cart.cases.all():
            order.cases.add(product)

        for product in cart.fan.all():
            order.fan.add(product)

        for product in cart.power_unit.all():
            order.power_unit.add(product)

        for product in cart.RAM.all():
            order.RAM.add(product)

        for product in cart.headphones.all():
            order.headphones.add(product)

        for product in cart.graphic_cards.all():
            order.graphic_cards.add(product)

        for product in cart.motherboards.all():
            order.motherboards.add(product)

        for product in cart.keyboard.all():
            order.keyboard.add(product)

        for product in cart.mouse.all():
            order.mouse.add(product)

        order.save()
        cart.delete()

        return Response({"data": {"message": "the order has been placed", "code": 201}})
