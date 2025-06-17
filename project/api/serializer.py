from rest_framework import serializers
from .models import product_models, user_models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_models.User
        fields = "__all__"

    def create(self, validated_data):
        user = user_models.User.objects.create(
            nik=validated_data["nik"],
            email=validated_data["email"]
        )

        user.set_password(validated_data["password"])
        user.save()

        return user


class ProcessorProdSerializer(serializers.Serializer):
    class Meta:
        model = product_models.Processor
        fields = "__all__"


class MotherboardProdSerializer(serializers.Serializer):
    class Meta:
        model = product_models.Processor
        fields = "__all__"


class RAMProdSerializer(serializers.Serializer):
    class Meta:
        model = product_models.Processor
        fields = "__all__"


class GraphicCardProdSerializer(serializers.Serializer):
    class Meta:
        model = product_models.Processor
        fields = "__all__"


class DiscProdSerializer(serializers.Serializer):
    class Meta:
        model = product_models.Processor
        fields = "__all__"


class CoolerProdSerializer(serializers.Serializer):
    class Meta:
        model = product_models.Processor
        fields = "__all__"


class CaseProdSerializer(serializers.Serializer):
    class Meta:
        model = product_models.Processor
        fields = "__all__"


class PowerUnitProdSerializer(serializers.Serializer):
    class Meta:
        model = product_models.Processor
        fields = "__all__"


class FanProdSerializer(serializers.Serializer):
    class Meta:
        model = product_models.Processor
        fields = "__all__"


class MonitorProdSerializer(serializers.Serializer):
    class Meta:
        model = product_models.Processor
        fields = "__all__"


class KeyboardProdSerializer(serializers.Serializer):
    class Meta:
        model = product_models.Processor
        fields = "__all__"


class MouseProdSerializer(serializers.Serializer):
    class Meta:
        model = product_models.Processor
        fields = "__all__"


class HeadphonesProdSerializer(serializers.Serializer):
    class Meta:
        model = product_models.Processor
        fields = "__all__"


class ProductsSerializer(serializers.Serializer):
    class Meta:
        model = product_models.Processor
        fields = "__all__"


class SavedPresetsSerializer(serializers.Serializer):
    class Meta:
        model = product_models.Processor
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    products = ProductsSerializer(many=True)

    class Meta:
        model = user_models.Cart
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    products = ProductsSerializer(many=True)

    class Meta:
        model = user_models.Order
        fields = ['id', 'order_price', 'products']
