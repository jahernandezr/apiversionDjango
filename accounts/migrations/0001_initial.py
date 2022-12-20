# Generated by Django 3.2.15 on 2022-11-28 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modulosusuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombremodulo', models.CharField(max_length=100)),
                ('urlaplicativo', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'modulosusuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Permisosaplicativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idmodulo', models.IntegerField()),
                ('idpermiso', models.IntegerField()),
            ],
            options={
                'db_table': 'permisosaplicativo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('first_apellido', models.CharField(max_length=50)),
                ('last_apellido', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]