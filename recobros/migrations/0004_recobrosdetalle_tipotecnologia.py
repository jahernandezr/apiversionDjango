# Generated by Django 4.1.3 on 2023-01-09 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recobros', '0003_recobrosdetalle_deschomologo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recobrosdetalle',
            name='tipoTecnologia',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
