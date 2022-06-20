# Generated by Django 4.0.5 on 2022-06-20 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jaime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('sexo', models.CharField(choices=[('F', 'femenino'), ('M', 'masculino')], max_length=1)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
    ]