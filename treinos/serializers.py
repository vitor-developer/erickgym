from rest_framework import serializers
from treinos.models import Exercicio


class ExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicio
        fields = ['id', 'nome', 'descricao',
                  'em_equipamento', 'idade_minima_aluno']