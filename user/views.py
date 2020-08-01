from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
from django.http import HttpResponse, JsonResponse
import json
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response


@csrf_exempt
def register(request):
    if request.method == "POST":
        print(request.body)
        json_data = json.loads(request.body)
        email = json_data['email']
        password = json_data['password']
        username = json_data['username']
        print(json_data)
        print(email)
        print(password)
        print(username)
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return Response(status=status.HTTP_201_CREATED)

@csrf_exempt
def loginAttempt(request):
    print(request.body)
    json_data = json.loads(request.body)
    email = json_data['email']
    password = json_data['password']
    username = json_data['username']
    print(json_data)
    print(email)
    print(password)
    print(username)
    user = authenticate(username=username, email=email, password=password)
    if user is not None:
        print('success log in')
        login(request, user)
        token = Token.objects.create(user=user)
        print(token.key)
        return Response(status=status.HTTP_202_CREATED)
    else:
        print('error log in')
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@csrf_exempt
def authenticationCheck(request):
    print(request.user)
    if request.user.is_authenticated:
        print("is auth")
        return HttpResponse("is authenticated")
    else:
        print("is not auth")
        return HttpResponse("is not authenticated")
