from rest_framework import serializers
from .models import Board
from user.models import User, UserInfo
from dormitory.models import Dormitory


class DormitorySerializer(serializers.ModelSerializer):

        users = serializers.SerializerMethodField()

        def get_users(self, obj):
                users = obj.userinfo_set.filter(dormitory=obj.id).values()
                return users

        class Meta:
                model = Dormitory
                fields = ["name", "desc", "logo", "users"]


class BoardSerializer(serializers.ModelSerializer):

        icon = serializers.SerializerMethodField()

        def get_icon(self, obj):
                try:
                        dorm_name = obj.author.userinfo.dormitory
                        dorm = Dormitory.objects.get(name=dorm_name)
                        icon = dorm.logo.url
                        return icon
                except:
                        return ''

        class Meta:
                model = Board
                fields = "__all__"


class LoungeSerializer(serializers.ModelSerializer):

        portrait = serializers.SerializerMethodField()
        dormitory_name = serializers.SerializerMethodField()

        def get_portrait(self, obj):
                portrait = obj.userinfo.portrait.url
                return portrait


        def get_dormitory_name(self, obj):
                dormitory_name = obj.userinfo.dormitory.name
                return dormitory_name

        class Meta:
                model = User
                fields = ["username", "fullname", "portrait", "dormitory_name"]