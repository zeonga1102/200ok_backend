from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from user.serializers import UserSerializer

from deeplearning.deeplearning_make_portrait import make_portrait
from multiprocessing import Process, Queue
from user.serializers import OriginalPicSerializer
# from dormitory.models import Question


class UserView(APIView):

    # 회원가입
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()

        return Response(user_serializer.data, status=status.HTTP_200_OK)


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


q = Queue()
p = None
class MainView(APIView):

    def get(self, requeset):
        return Response({'msg': 'success'})
    
    def post(self, request):
        global q, p

        request.data['user'] = request.user.id
        print(request.data)

        original_pic_serializer = OriginalPicSerializer(data=request.data)

        if original_pic_serializer.is_valid():
            original_pic_serializer.save()
            path = f'media/original/' + request.data.get('pic').name

            p = Process(target=make_portrait, args=(q, path,))
            p.start()

            return Response({'msg': 'send'}, status=status.HTTP_200_OK)

        print(original_pic_serializer.error_messages)

        return Response({"error": "failed"}, status=status.HTTP_400_BAD_REQUEST)



class InfoView(APIView):

    def get(self, request):
        # questions = Question.objects.all()
        # question_serializer = QuestionSerializer(questions, many=True).data
        return Response({'msg': 'get'}, status=status.HTTP_200_OK)

    def post(self, request):
        global p, q

        if p is not None:
            p.join()
            print('q: ', q.get())
            return Response({'msg': 'post'}, status=status.HTTP_200_OK)
        
        return Response({'error': 'failed'}, status=status.HTTP_400_BAD_REQUEST)
