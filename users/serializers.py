from rest_framework import serializers
from .models import User,UserConfirm


class UserRegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class UserLoginSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=30, write_only=True)


class UserConfirmSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserConfirm
        fields = ('code',)
