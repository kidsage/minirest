from turtle import ondrag
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone


# Create your models here.
class UserManager(BaseUserManager):    

    use_in_migrations = True    

    def create_user(self, email, organization, password):        
        
        if not email:            
            raise ValueError('이메일을 등록해주세요.')
        if not password:            
            raise ValueError('패스워드를 등록해주세요.')

        user = self.model(
            email=self.normalize_email(email),
            organization=organization
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, organization, password):        

        user = self.create_user(            
            email = self.normalize_email(email),                    
            password=password,

        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user 


class User(AbstractBaseUser, PermissionsMixin):    
   
    objects = UserManager()

    email = models.EmailField(        
        max_length=255,        
        unique=True,    
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'    
    # REQUIRED_FIELDS = ['organization']

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin