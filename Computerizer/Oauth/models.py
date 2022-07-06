from django.db import models
from django import forms
# Create your models here.

from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
    AbstractBaseUser
    )
from django.forms import Widget
class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None,is_active=True,is_staff=False,is_admin=False):
        if not email:
            raise ValueError('User Must Have Email')
        if not password:
            raise ValueError('User Must Have Password')
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)#change user password
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)   
        return user_obj
    def create_staffuser(self,email,password=None):
        user = self.create_user(
            email,
            password = password,
            is_staff = True
        )
        return user
    def create_superuser(self,email,password=None):
        user = self.create_user(
            email,
            password = password,
            is_staff = True,
            is_admin = True,
        )
        return user
class CustomUser(AbstractBaseUser):
    first_name        = models.CharField(max_length = 300)
    last_name         = models.CharField(max_length = 300)
    email             = models.EmailField(max_length=255,unique=True)
    username          = models.CharField(max_length= 200)
    password          = models.CharField(max_length=100,)
    password_2        = models.CharField(max_length=100,)
    sub_to_newsletter = models.BooleanField(default=True)
    own_pc            = models.BooleanField(default=False) 
    active            = models.BooleanField(default=True)  #can login
    staff             = models.BooleanField(default=False) #staff user not superuser
    admin             = models.BooleanField(default=False) #admin / superuser
    
    USERNAME_FIELD  = 'email' #username
    #email and password is requierd by default
    REQUIRED_FIELDS = [] #python manage.py createsuperuser
    objects = CustomUserManager()

    def __str__(self):
        return self.email
    def get_full_name(self):
        return self.email
    def get_short_name(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        return self.staff
    @property
    def is_admin(self):
        return self.admin
    @property
    def is_active(self):
        return self.active

    pass