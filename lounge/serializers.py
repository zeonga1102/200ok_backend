from rest_framework import serializers
from .models import Board
from user.models import User, UserInfo
from dormitory.models import Dormitory
from django.utils import timezone, dateformat


class DormitorySerializer(serializers.ModelSerializer):

        users = serializers.SerializerMethodField(read_only=True)

        def get_users(self, obj):
                users = obj.userinfo_set.filter(dormitory=obj.id).values()

                for user in users:
                        portrait = user['portrait']
                        # 추후 url이 달라질 때 어떻게 자동으로 추적하게 해줘야 하려나?
                        user['portrait'] = f'/media/{portrait}'

                return users

        class Meta:
                model = Dormitory
                fields = ["name", "desc", "logo", "users"]


class BoardSerializer(serializers.ModelSerializer):

        icon = serializers.SerializerMethodField(read_only=True)

        def get_icon(self, obj):
                try:
                        dorm_name = obj.author.userinfo.dormitory
                        dorm = Dormitory.objects.get(name=dorm_name)
                        icon = dorm.logo.url
                        return icon
                except:
                        return ''
        
        def validate(self, data):
                if len(data.get('content')) <= 5:
                         raise serializers.ValidationError(
                                detail={"error": "5글자를 넘아야 합니다."},
                                )

                return data

        def create(self, validated_data):
                cemment = Board(**validated_data)
                cemment.save()

                return validated_data

        def update(self, instance, validated_data):
                formatted_date = dateformat.format(timezone.now(), 'y.m.d H:i')

                for key, value in validated_data.items():
                        if key == 'content':
                                value = value + f' ({formatted_date} 수정)'
                                setattr(instance, key, value)
                instance.save()

                return instance

        class Meta:
                model = Board
                fields = "__all__"


class LoungeSerializer(serializers.ModelSerializer):

        portrait = serializers.SerializerMethodField(read_only=True)
        dormitory_name = serializers.SerializerMethodField(read_only=True)

        def get_portrait(self, obj):
                portrait = obj.userinfo.portrait.url
                return portrait

        def get_dormitory_name(self, obj):
                dormitory_name = obj.userinfo.dormitory.name
                return dormitory_name

        class Meta:
                model = User
                fields = ["id", "username", "fullname", "portrait", "dormitory_name"]