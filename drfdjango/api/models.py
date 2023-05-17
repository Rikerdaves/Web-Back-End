from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


def nivel(value):
    if value not in [1, 3, 5, 8]:
        raise ValidationError('Valor inválido')
    
def prioridade(value):
    if value not in [1, 2, 3]:
        raise ValidationError('Valor inválido')

SITUACAO_CHOICES = (
    ('nova', 'Nova'),
    ('em andamento', 'Em andamento'),
    ('pendente', 'Pendente'),
    ('resolvida', 'Resolvida'),
    ('cancelado', 'Cancelado'),
)

User = get_user_model()


class Tarefas(models.Model):
    descricao = models.CharField()
    responsavel = models.CharField()
    nivel = models.PositiveIntegerField(validators=[nivel])
    prioridade = models.PositiveIntegerField(validators=[prioridade])
    situacao = models.CharField(choices=SITUACAO_CHOICES)
    usuario = models.ForeignKey(
        User, related_name='tarefas', on_delete=models.SET_NULL, null=True, default=None)
    