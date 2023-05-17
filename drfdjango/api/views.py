from django.shortcuts import render

from rest_framework .response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated

from api.models import Tarefas
from api.serializers import TarefasSerializer, UserSerializer

class Hello(APIView):
    def get(self, request):
        return Response({'Message': 'Hello Django + DRF'})

class TarefasList(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tarefa = Tarefas.objects.filter(usuario=request.user)
        serializer = TarefasSerializer(tarefa, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TarefasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['usuario'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class DetailUpdateDelete(APIView):
        
    permission_classes = [IsAuthenticated]

    def get_tarefas(self, pk, usuario):
        try:
            return Tarefas.objects.get(pk=pk, usuario=usuario)
        except Tarefas.DoesNotExist:
            raise Http404    
    
    def get(self, request, pk):
        filme = self.get_tarefas(pk, request.user)
        serializer = TarefasSerializer(filme)
        return Response(serializer.data)

    def put(self, request, pk):
        tarefa = self.get_tarefas(pk, request.user)
        serializer = TarefasSerializer(tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tarefa = self.get_tarefas(pk, request.user)
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserSignup(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)            