from django.urls import path , include
from . import views

urlpatterns = [

    path('', views.getRoutes, name='routes'),
    path('choices/', views.getChoices, name='Choices'),
    path('choices/<str:pk>/', views.getChoice, name='Choice'),
]
