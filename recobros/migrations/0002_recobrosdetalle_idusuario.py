# Generated by Django 4.1.3 on 2023-01-09 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recobros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recobrosdetalle',
            name='idusuario',
            field=models.IntegerField(null=True),
        ),
    ]
