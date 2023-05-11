from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from api.models import Tarefas

class TarefasSerializer(ModelSerializer):

    class Meta:
        model = Tarefas
        fields = '__all__'