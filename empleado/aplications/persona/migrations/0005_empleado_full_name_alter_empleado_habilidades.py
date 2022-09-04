# Generated by Django 4.1 on 2022-08-23 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0004_alter_habilidad_options_empleado_hoja_vida'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='Full name'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(blank=True, to='persona.habilidad'),
        ),
    ]
