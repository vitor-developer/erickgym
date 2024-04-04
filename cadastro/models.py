from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=150,null=False,blank=False) 
    sexo = models.CharField(max_length=1, choices=(('M', 'Masculino'), ('F', 'Feminino')),null=False,blank=False)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15,null=False,blank=False)
    cpf = models.CharField(max_length=11,null=False,blank=False)

    def __str__(self):
        return f'Nome: {self.nome}| Sexo: {self.sexo} | Data de Nascimento: {self.data_nascimento} | Telefone: {self.telefone} | Cpf: {self.cpf} '

class Professor(models.Model):
    cpf = models.CharField(max_length=14, null=False, blank=False)
    nome = models.CharField(max_length=200, null=False, blank=False)
