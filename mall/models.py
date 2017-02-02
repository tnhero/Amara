from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, first_name, last_name, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not email:
            raise ValueError('The email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, first_name, last_name, password, **extra_fields)

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, first_name, last_name, password, **extra_fields)





class Owner(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    owner_image = models.ImageField(upload_to= '/avatar/%Y/%m/%d')


class Store (models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    store_name = models.CharField(max_length= 30)
    store_logo = models.ImageField(upload_to= '/store-logo/%Y/%m/%d')
    address1 = models.CharField(max_length=100, blank=False)
    address2 = models.CharField(max_length=100, blank=True)
    telephone = models.IntegerField(max_length=13)
    email= models.EmailField(max_length=60)


class Item (models.Model):
    item_mame = models.CharField(max_length= 30)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    price= models.IntegerField()
    details = models.CharField(max_length=1000)
    photo1 = models.ImageField(upload_to= '/item/%Y/%m/%d', blank=False)
    photo2 = models.ImageField(upload_to='/item/%Y/%m/%d', blank=True)
    photo3 = models.ImageField(upload_to='/item/%Y/%m/%d', blank=True)


class Buyer (models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=60)
    telephone = models.IntegerField(max_length=13)
    address1 = models.CharField(max_length=100, blank=False)
    address2 = models.CharField(max_length=100, blank=True)
