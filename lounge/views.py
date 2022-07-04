import django.apps
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.shortcuts import render, redirect

from .serializers import BoardSerializer, LoungeSerializer, DormitorySerializer, DormitoriesSerializer
from .models import Board
from user.models import User, UserInfo
from dormitory.models import Dormitory


class LoungeView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    # TODO  라운지 페이지 띄우기
    def get(self, request):
        user = request.user
        userinfo = User.objects.filter(id=user.id)
        userdorm = Dormitory.objects.filter(name=user.userinfo.dormitory.name)
        dorm = Dormitory.objects.all()
        dorm_count = dorm.count()
        board = Board.objects.all().order_by('-created')

        lounge_serialrzer = LoungeSerializer(userinfo, many=True).data
        dormitory_serializer = DormitorySerializer(userdorm, many=True).data
        dormitories_serializer = DormitoriesSerializer(dorm, many=True).data
        board_serializer = BoardSerializer(board, many=True).data

        dorm_name_list = [dormitories_serializer[i]['name'] for i in range(dorm_count)]
        dorm_users_count_list = [dormitories_serializer[i]['users'].count() for i in range(dorm_count)]
                        
        dormitory_serializer[0]['users'] = dormitory_serializer[0]['users'].exclude(user_id=user.id)

        if len(dormitory_serializer[0]['users']) >= 5:
                dormitory_serializer[0]['users'] = dormitory_serializer[0]['users'][:5]

        for user in dormitory_serializer[0]['users']:
                portrait = user['portrait']
                # 추후 url이 달라질 때 어떻게 자동으로 추적하게 해줘야 하려나?
                user['portrait'] = f'/media/{portrait}'

        lounge_data = {
            "user": lounge_serialrzer,
            "house": dormitory_serializer,
            "count": {
                "label": dorm_name_list,
                "data": dorm_users_count_list
            },
            "board": board_serializer
        }

        return render(request, 'lounge/lounge.html', {"lounge_data":lounge_data}, status=status.HTTP_200_OK)

    # TODO 게시글 쓰기
    def post(self, request):
        request_data = request.data.copy()
        request_data['author'] = request.user.id
        board_serializer = BoardSerializer(data=request_data)

        if board_serializer.is_valid():
            board_serializer.save()
            return redirect('lounge')

        return Response(board_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # TODO 게시글 수정
    def put(self, request, obj_id):
        comment = Board.objects.get(id=obj_id)
        board_serializer = BoardSerializer(comment, data=request.data, partial=True)
        print(f'author: {comment.author}, user: {request.user.username}')

        if comment.author == request.user:
            if board_serializer.is_valid():
                board_serializer.save()
                return redirect('lounge')
            return Response(board_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': '이 글을 작성한 사람이 아닙니다!'}, status=status.HTTP_400_BAD_REQUEST)

    # TODO 게시글 삭제
    def delete(self, request, obj_id):
        comment = Board.objects.get(id=obj_id)

        if comment.author == request.user:
            comment.delete()
            return redirect('lounge')

        return Response({'message': '이 글을 작성한 사람이 아닙니다!'}, status=status.HTTP_400_BAD_REQUEST)