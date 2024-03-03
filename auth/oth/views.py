from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .Serializer import *
from .models import *


# Create your views here.
def login(request):
    return render(request,'login.html')
# @login_required
