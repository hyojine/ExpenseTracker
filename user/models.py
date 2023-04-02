from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('User must have an email') 
        if not password:
            raise ValueError('User must have a password') 
        if username=='':
            username=email.split('@')[0]
            print(username)
        instance = self.model(
            email=email,
            username=username
        )
        instance.set_password(password) #해싱
        instance.save(using=self._db)
        return instance

    def create_superuser(self, email, username, password=None):
    
        instance = self.create_user(
            email = email,
            password=password,
            username=username,
        )
        instance.is_admin = True
        instance.save(using=self._db)
        return instance
    
class Users(AbstractBaseUser):
    email = models.EmailField('이메일', unique=True, error_messages={"unique":"이미 사용중인 이메일입니다"})
    password = models.CharField('비밀번호',max_length=30, blank=False, null=False)
    username = models.CharField('회원이름',max_length=30, blank=True, null=False)
    is_active = models.BooleanField('회원상태',default=True)
    is_admin = models.BooleanField('관리자여부',default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the instance have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the instance have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the instance a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


