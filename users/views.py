from django.contrib.auth import login, logout
from django.shortcuts import render, HttpResponseRedirect, redirect
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib import messages

from users.serializers import LoginSerializer


class UserLogin(APIView):

    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            login(request, user)
            messages.success(request, 'login successful')
            return redirect('books:get_books')
        except Exception as e:
            messages.error(request, str(e))
            return HttpResponseRedirect('login')


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_logout(request):
    logout(request)
    return Response('User Logged out successfully')