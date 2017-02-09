from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, first_name, last_name, password, is_staff, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.is_staff = is_staff
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, first_name, last_name, password, **extra_fields)

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        is_staff = True
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, first_name, last_name, password, is_staff, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('first name', max_length=30)
    last_name = models.CharField('last name', max_length=30)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField(default=False)
    phone_regex = RegexValidator(regex=r'^\+?234?\d{10}$',
                                 message="Phone number must be in the format: '+234...'. Up to 13 digits allowed.")
    telephone = models.CharField(validators=[phone_regex], blank=True)  # validators should be a list
    address1 = models.CharField(max_length=1000, blank=True)
    address2 = models.CharField(max_length=1000, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Owner(User):
    owner_image = models.ImageField(upload_to='/avatar/%Y/%m/%d')


class Store (models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    store_name = models.CharField(max_length= 30)
    store_logo = models.ImageField(upload_to= '/store-logo/%Y/%m/%d')
    address1 = models.CharField(max_length=100, blank=False)
    address2 = models.CharField(max_length=100, blank=True)
    telephone = models.IntegerField()
    email= models.EmailField(max_length=60)


class Item (models.Model):
    item_mame = models.CharField(max_length= 30)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    price= models.IntegerField()
    details = models.CharField(max_length=1000)
    photo1 = models.ImageField(upload_to= '/item/%Y/%m/%d', blank=False)
    photo2 = models.ImageField(upload_to='/item/%Y/%m/%d', blank=True)
    photo3 = models.ImageField(upload_to='/item/%Y/%m/%d', blank=True)
