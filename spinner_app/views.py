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
            'Endpoint': '/choices/view/id',
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
            'Endpoint': '/choices/view/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing choice with data sent in post request'
        },
        {
            'Endpoint': '/choices/view/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting choice'
        },
    ]
    return Response(routes)

# get all choices
@api_view(['GET'])
def getChoices(request):
    choices = Choice.objects.all().order_by('-updated')
    serializer = ChoicesSerializer(choices, many=True)
    return Response(serializer.data)

# get a single choice
@api_view(['GET'])
def getChoice(request, pk):
    choices = Choice.objects.get(id=pk)
    serializer = ChoicesSerializer(choices, many=False)
    return Response(serializer.data)

# Creat choice
@api_view(['POST'])
def creatChoice(request):
    data = request.data
    choice = Choice.objects.create(
        body=data['body']
    )
    serializer = ChoicesSerializer(choice,many=False)
    return Response(serializer.data)


# update choice
@api_view(['PUT'])
def updateChoice(request, pk):
   data = request.data
   choice = Choice.objects.get(id=pk)
   serializer = ChoicesSerializer(instance=choice , data=data)

   if serializer.is_valid():
    serializer.save()

   return Response(serializer.data)



# Delete Choice
@api_view(['DELETE'])
def deleteChoice(request, pk):
    choice = Choice.objects.get(id=pk)
    choice.delete()
    return Response("Deleted Choice"+id)