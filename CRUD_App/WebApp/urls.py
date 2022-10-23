from django.contrib import admin
from django.urls import path , include
from . import views

# Write Your Pattern Here.
urlpatterns = [
    path('',views.HomeView,name="Home"),
    path('update/<int:id>/',views.UpdateView,name='Update'),
    path('delete/<int:id>/',views.DeleteView,name='Delete'),
    
]
