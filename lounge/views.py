import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from .serializers import BoardSerializer, LoungeSerializer, DormitorySerializer
from .models import Board
from user.models import User, UserInfo
from dormitory.models import Dormitory


# Create your views here.
class LoungeView(APIView):
        permission_classes = [permissions.IsAuthenticated]

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
                dormitories_serializer = DormitorySerializer(dorm, many=True).data
                board_serializer = BoardSerializer(board, many=True).data

                dorm_name_list = [ dormitories_serializer[i]['name'] for i in range(dorm_count) ]
                dorm_users_count_list =  [ dormitories_serializer[i]['users'].count() for i in range(dorm_count) ]

                lounge_data = {
                        "user": lounge_serialrzer,
                        "house": dormitory_serializer,
                        "count":{
                                "label":dorm_name_list, 
                                "data":dorm_users_count_list
                                },
                        "board":board_serializer
                }

                return Response(lounge_data, status=status.HTTP_200_OK)

        # TODO 게시글 쓰기
        def post(self, request):
                request.data['author'] = request.user.id
                board_serializer = BoardSerializer(data=request.data)

                if board_serializer.is_valid():
                        board_serializer.save()
                        return Response({"message": "정상"}, status=status.HTTP_200_OK)
        
                return Response(board_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # TODO 게시글 수정
        def put(self, request, obj_id):
                comment = Board.objects.get(id=obj_id)
                board_serializer = BoardSerializer(comment, data=request.data, partial=True)
                print(f'author: {comment.author}, user: {request.user.username}')

                if comment.author == request.user:
                        if board_serializer.is_valid():
                                board_serializer.save()
                                return Response({"message": "정상"}, status=status.HTTP_200_OK) 
                        return Response(board_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                return Response({'message':'이 글을 작성한 사람이 아닙니다!'}, status=status.HTTP_400_BAD_REQUEST)

        # TODO 게시글 삭제
        def delete(self, request, obj_id):
                comment = Board.objects.get(id=obj_id)

                if comment.author == request.user:
                        comment.delete()
                        return Response({"message": "정상"}, status=status.HTTP_200_OK)
                
                return Response({'message':'이 글을 작성한 사람이 아닙니다!'}, status=status.HTTP_400_BAD_REQUEST)