from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import render
from dormitory.serializers import DormUserSerializer
from user.models import User, UserInfo


class DormitoryView(APIView):
    def get(self, request):
        user = request.user
        # user = User.objects.get(id=6)
        # dormitory = UserInfo.objects.get(user=user).dormitory
        # print(dormitory.name, dormitory.id)

        return Response(DormUserSerializer(user).data)