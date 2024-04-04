# Generated by Django 5.0.3 on 2024-04-04 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('data_nascimento', models.DateField()),
                ('telefone', models.CharField(max_length=15)),
                ('cpf', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=14)),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
    ]
