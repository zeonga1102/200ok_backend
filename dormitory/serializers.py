from dataclasses import field
from rest_framework import serializers
from user.models import User, UserInfo


class DormUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['birthday', 'portrait', 'dormitory']


class DormUserSerializer(serializers.ModelSerializer):
    birthday = serializers.SerializerMethodField()
    portrait = serializers.SerializerMethodField()
    dormitory = serializers.SerializerMethodField()
    dormitory_id = serializers.SerializerMethodField()

    def get_birthday(self, obj):
        return obj.userinfo.birthday

    def get_dormitory_id(self, obj):
        return obj.userinfo.dormitory.id

    def get_dormitory(self, obj):
        return obj.userinfo.dormitory.name

    def get_portrait(self, obj):
        return obj.userinfo.portrait.url

    class Meta:
        model = User
        fields = ['id', 'fullname', 'dormitory_id', 'dormitory', 'portrait', 'birthday', 'join_date']