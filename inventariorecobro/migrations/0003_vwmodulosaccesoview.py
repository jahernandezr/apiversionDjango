# Generated by Django 4.1.3 on 2022-12-30 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

# initial = False

    dependencies = [
        ('inventariorecobro', '0002_prestadoressuludvida'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vwmodulosaccesoview',
            fields=[
                ('id', models.IntegerField(db_column='id', primary_key=True, serialize=False)),
                ('nombremodulo', models.CharField(db_column='nombremodulo', max_length=100)),
                ('urlaplicativo', models.CharField(db_column='urlaplicativo', max_length=100)),
                ('email', models.CharField(db_column='email', max_length=100)),
            ],
            options={
                'db_table': 'vwmodulosacceso',
                'managed': False,
            },
        ),
    ]
