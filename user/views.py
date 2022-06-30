from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from user import serializers

from user.serializers import UserSerializer


class UserView(APIView):

    # 회원가입
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()
            return Response({"messages" : "가입 성공"})
            # return Response(user_serializer.data, status=status.HTTP_200_OK)

        else:
            print(serializers.errors)
            return Response({"messages" : "가입 실패"})


class UserAPIView(APIView):

    # 로그인
    def post(self, request):
        # username = request.data.get('username', '')
        # password = request.data.get('password', '')

        # user = authenticate(request, username=username, password=password)
        user = authenticate(request, **request.data)
        if not user:
            return Response({"error": "잘못된 아이디 혹은 비밀번호입니다."},
                            status=status.HTTP_400_BAD_REQUEST)
        login(request, user)

        return Response({"messages": "로그인 성공"})

    # 로그아웃
    def delete(self, request):
        logout(request)
        return Response({"messages": "로그아웃  성공"})