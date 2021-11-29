# Generated by Django 3.2.8 on 2021-11-05 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
        migrations.CreateModel(
            name='tessiu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Temperatura', models.FloatField(verbose_name='Temperatura')),
                ('Color', models.FloatField()),
                ('Inflamation', models.FloatField(verbose_name='Inflamacion')),
                ('Nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.paciente')),
            ],
            options={
                'verbose_name': 'tejido',
                'verbose_name_plural': 'Tejidos',
            },
        ),
    ]