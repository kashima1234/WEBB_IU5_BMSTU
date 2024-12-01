from rest_framework import serializers

from . import utils
from .models import *


class PlaceSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, place):
        if place.image:
            return place.image.url.replace("minio", "localhost", 1)

        return "http://localhost:9000/images/default.png"

    class Meta:
        model = Place
        fields = "__all__"


class PlaceItemSerializer(utils.CustomSerializer):
    image = serializers.SerializerMethodField()
    value = serializers.SerializerMethodField('get_value')
    calc = serializers.SerializerMethodField()

    def get_image(self, place):
        if place.image:
            return place.image.url.replace("minio", "localhost", 1)

        return "http://localhost:9000/images/default.png"

    def get_value(self, place):
        return self.context.get("value")

    def get_calc(self, place):
        return self.context.get("calc")

    class Meta:
        model = Place
        fields = ("id", "name", "image", "value", "calc")


class ExpeditionsSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    moderator = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Expedition
        fields = "__all__"


class ExpeditionSerializer(serializers.ModelSerializer):
    places = serializers.SerializerMethodField()
    owner = serializers.StringRelatedField(read_only=True)
    moderator = serializers.StringRelatedField(read_only=True)

    def get_places(self, expedition):
        items = PlaceExpedition.objects.filter(expedition=expedition)
        if expedition.status == 3:
            return [PlaceItemSerializer(item.place, context={"value": item.value, "calc": item.calc}).data for item in items]

        return [PlaceItemSerializer(item.place, context={"value": item.value}, excluded_fields=("calc", )).data for item in items]
    
    class Meta:
        model = Expedition
        fields = "__all__"


class PlaceExpeditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceExpedition
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username')


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'username')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)