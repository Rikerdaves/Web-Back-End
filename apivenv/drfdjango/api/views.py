from django.shortcuts import render

from rest_framework .response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

from api.models import Tarefas
from api.serializers import TarefasSerializer

class Hello(APIView):
    def get(self, request):
        return Response({'Message': 'Hello Django + DRF'})

class CreateTarefas(APIView):
    def get(self, request):
        serializer = TarefasSerializer(Tarefas.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TarefasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)