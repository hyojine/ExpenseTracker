from django.shortcuts import redirect
from rest_framework import permissions
from .models import Users
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from user.serializers import MyTokenObtainPairSerializer, SignUpSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.
class LogInView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class SignUpView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message":"회원가입이 완료되었습니다!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"회원가입에 실패했습니다. 다시 시도해주세요"}, status=status.HTTP_400_BAD_REQUEST)





