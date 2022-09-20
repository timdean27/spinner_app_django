from rest_framework.response import Response
from .models import Choice
from .serializers import ChoicesSerializer


def getChoicesList(request):
    choices = Choice.objects.all().order_by('-updated')
    serializer = ChoicesSerializer(choices, many=True)
    return Response(serializer.data)


def getChoiceDetail(request, pk):
    choices = Choice.objects.get(id=pk)
    serializer = ChoicesSerializer(choices, many=False)
    return Response(serializer.data)


def createChoice(request):
    data = request.data
    choice = Choice.objects.create(
        body=data['body']
    )
    serializer = ChoicesSerializer(choice, many=False)
    return Response(serializer.data)

def updateChoice(request, pk):
    data = request.data
    choice = Choice.objects.get(id=pk)
    serializer = ChoicesSerializer(instance=choice, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


def deleteChoice(request, pk):
    choice = Choice.objects.get(id=pk)
    choice.delete()
    return Response("Deleted Choice")