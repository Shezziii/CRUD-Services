from django.shortcuts import render
from django.http import JsonResponse
from .serializers import UserCreate
from rest_framework.decorators import api_view
import io
# Create your views here.
@api_view(['POST' , ])
def ApiViewHome(request):
    if request.method=='POST':
        stream=request.data
        user=UserCreate(data=stream)
        if user.is_valid(raise_exception=True):
            #print(user.data)
            Data=user.save()
            return JsonResponse(data=Data)
    return JsonResponse({'Error':  'Not Working.'})