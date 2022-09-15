from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Choice
from .serializers import ChoicesSerializer
# Create your views here.

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/choices/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of choices'
        },
        {
            'Endpoint': '/choices/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single choice object'
        },
        {
            'Endpoint': '/choices/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new choice with data sent in post request'
        },
        {
            'Endpoint': '/choices/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing choice with data sent in post request'
        },
        {
            'Endpoint': '/choices/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting choice'
        },
    ]
    return Response(routes)

# get all choices
@api_view(['GET'])
def getChoices(request):
    choices = Choice.objects.all()
    serializer = ChoicesSerializer(choices, many=True)
    return Response(serializer.data)

# get a single choice
@api_view(['GET'])
def getChoice(request, pk):
    choices = Choice.objects.get(id=pk)
    serializer = ChoicesSerializer(choices, many=False)
    return Response(serializer.data)
