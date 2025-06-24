# сериализация всех моделей приложения

from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"

    def create(self, validated_data):
        user = models.User.objects.create(
            nik=validated_data["nik"],
            email=validated_data["email"]
        )

        user.set_password(validated_data["password"])
        user.save()

        return user


class ProcessorProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Processor
        fields = "__all__"


class MotherboardProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Motherboard
        fields = "__all__"


class RAMProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RAM
        fields = "__all__"


class GraphicCardProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GraphicCard
        fields = "__all__"


class DiscProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Disc
        fields = "__all__"


class CoolerProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cooler
        fields = "__all__"


class CaseProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Case
        fields = "__all__"


class PowerUnitProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PowerUnit
        fields = "__all__"


class FanProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fan
        fields = "__all__"


class MonitorProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Monitor
        fields = "__all__"


class KeyboardProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Keyboard
        fields = "__all__"


class MouseProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mouse
        fields = "__all__"


class HeadphonesProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Headphones
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    processors = ProcessorProdSerializer(many=True)
    graphic_cards = GraphicCardProdSerializer(many=True)
    motherboards = MotherboardProdSerializer(many=True)
    RAM = RAMProdSerializer(many=True)
    discs = DiscProdSerializer(many=True)
    coolers = CoolerProdSerializer(many=True)
    cases = CaseProdSerializer(many=True)
    power_unit = PowerUnitProdSerializer(many=True)
    fan = FanProdSerializer(many=True)
    monitor = MonitorProdSerializer(many=True)
    keyboard = KeyboardProdSerializer(many=True)
    mouse = MouseProdSerializer(many=True)
    headphones = HeadphonesProdSerializer(many=True)

    class Meta:
        model = models.Cart
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    processors = ProcessorProdSerializer(many=True)
    graphic_cards = GraphicCardProdSerializer(many=True)
    motherboards = MotherboardProdSerializer(many=True)
    RAM = RAMProdSerializer(many=True)
    discs = DiscProdSerializer(many=True)
    coolers = CoolerProdSerializer(many=True)
    cases = CaseProdSerializer(many=True)
    power_unit = PowerUnitProdSerializer(many=True)
    fan = FanProdSerializer(many=True)
    monitor = MonitorProdSerializer(many=True)
    keyboard = KeyboardProdSerializer(many=True)
    mouse = MouseProdSerializer(many=True)
    headphones = HeadphonesProdSerializer(many=True)

    class Meta:
        model = models.Order
        fields = "__all__"
