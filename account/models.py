import uuid

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import  AbstractUser
# from django.contrib.auth.base_user import  AbstractBaseUser

from django.utils import timezone

from .manager import CustomUserManager

# Create your models here.
class User(AbstractUser, PermissionsMixin):
        
      # These fields tie to the roles!
    ADMIN = 1
    MANAGER = 2
    SALES = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (SALES, 'SALES')
    )
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

  # Roles created here
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
    username = models.CharField(max_length=40,unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    created_by = models.EmailField()
    modified_by = models.EmailField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username