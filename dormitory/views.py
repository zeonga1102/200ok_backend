from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import render
from dormitory.serializers import DormUserSerializer
from user.models import UserInfo


# Create your views here.
class MyRoomView(APIView):
    def get(self, request):
        user = request.user

        return Response(DormUserSerializer(user).data)


class DormitoryView(APIView):
    def get(self, request):
        user = request.user
        dormitory = UserInfo.objects.get(user=user).dormitory
        print(dormitory.name, dormitory.id)

        return Response({'dormitory_name': dormitory.name, 'dormitory_id': dormitory.id})
        # return render(request, 'room/dormitory.html', {'dormitory': dormitory})

