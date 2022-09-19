from django.urls import path , include
from . import views

urlpatterns = [

    path('', views.getRoutes, name='routes'),
    path('choices/', views.getChoices, name='Choices'),
    path('choices/view/<str:pk>/update', views.updateChoice, name='updateChoice'),
    path('choices/view/<str:pk>/delete', views.deleteChoice, name='deleteChoice'),


    path('choices/view/<str:pk>/', views.getChoice, name='Choice'),

]
