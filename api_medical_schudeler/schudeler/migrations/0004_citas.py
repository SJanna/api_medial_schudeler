# Generated by Django 4.2.1 on 2023-05-29 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schudeler', '0003_remove_persona_correo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sede', models.CharField(max_length=200)),
                ('fecha_hora', models.DateTimeField()),
                ('cita_id', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schudeler.persona')),
            ],
        ),
    ]
