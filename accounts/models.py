from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
# para crear  la funcion de un nuevo usuario
class MyAccountManager(BaseUserManager):
    def create_user(self, email,first_name,last_name,username, password=None):
        if not email:
            raise ValueError('El usuario debe ingresar un email')

        if not username:
            raise ValueError('El usuario debe tener un Username')

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            username= username,
            password = password,
        )

        user.set_password(password)
        user.save(using=self._db)
        return  user

    def create_superuser(self, email,first_name,last_name,username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            username= username,
            password = password,
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return  user

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    first_apellido = models.CharField(max_length=50)
    last_apellido = models.CharField(max_length=50)
    username = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=100, unique=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name' ,'last_name','password']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return  True
class Modulosusuario(models.Model):
    nombremodulo = models.CharField(max_length=100)
    urlaplicativo = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'modulosusuario'


class Permisosaplicativo(models.Model):
    idmodulo = models.IntegerField()
    idpermiso = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'permisosaplicativo'

# class Vwmodulosaccesoview(models.Model):
#     id = models.IntegerField(db_column='id', primary_key=True)
#     nombremodulo = models.CharField(db_column='nombremodulo', max_length=100)
#     urlaplicativo = models.CharField(db_column='urlaplicativo', max_length=100)
#     email = models.CharField(db_column='email', max_length=100)
#
#     class  Meta:
#         managed = False
#         db_table = 'vwmodulosacceso'
