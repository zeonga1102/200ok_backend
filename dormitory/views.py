from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from dormitory.serializers import DormUserSerializer
from user.models import User, UserInfo


class DormitoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        return Response(DormUserSerializer(user).data)