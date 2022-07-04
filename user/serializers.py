from dataclasses import fields
from django.forms import PasswordInput
from rest_framework import serializers

from user.models import User as UserModel

from user.models import OriginalPic


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["username", "password", "fullname", ]

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = UserModel(**validated_data)
        # set_password() 를 사용해 헤싱을 해준다.
        user.set_password(password)
        user.save()

        return user


class OriginalPicSerializer(serializers.ModelSerializer):
    class Meta:
        model = OriginalPic
        fields = ["user", "pic"]