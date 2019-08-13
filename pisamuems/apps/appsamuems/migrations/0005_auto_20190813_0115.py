# Generated by Django 2.2.4 on 2019-08-13 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appsamuems', '0004_paciente_medicamentos'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmergenciaSnippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagonostico', models.CharField(max_length=50)),
                ('destino', models.CharField(max_length=255)),
                ('sintomas', models.CharField(blank=True, max_length=255)),
                ('equipos', models.CharField(blank=True, max_length=255)),
                ('fechaReporte', models.DateTimeField(auto_now_add=True)),
                ('estadoEmergencia', models.CharField(choices=[('T', 'Terminada'), ('E', 'En curso'), ('C', 'Cancelada'), ('L', 'Libre')], default='L', max_length=1)),
                ('comentarios', models.CharField(blank=True, max_length=255)),
                ('ambulancia', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='appsamuems.Ambulancia')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='appsamuems.Hospital')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='appsamuems.Paciente')),
            ],
        ),
    ]