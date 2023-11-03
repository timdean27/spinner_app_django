# spinner_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ChoiceList.as_view(), name='choice-list'),
    path('<int:pk>/', views.ChoiceDetail.as_view(), name='choice-detail'),
    
]
