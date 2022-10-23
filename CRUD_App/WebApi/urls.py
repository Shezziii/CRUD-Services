from django.contrib import admin
from django.urls import path , include
from . import views


urlpatterns = [
    path('',views.ApiViewHome,name="ApiHome"),
    #path('api/',include('WebApi.urls')),
]
