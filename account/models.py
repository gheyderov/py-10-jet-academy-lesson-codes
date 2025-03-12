from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import AbstractModel
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    ips = ArrayField(models.GenericIPAddressField(), null=True, blank=True) # 127.0.0.1 -> ipv4
    email = models.EmailField("email address", unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = '',

    def get_profile_image(self):
        if self.image:
            return self.image.url
        return '/static/images/profile.jpg/'
    

class BlockIpAddress(AbstractModel):
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.ip_address


class UserAddress(AbstractModel):
    address = models.CharField('address', max_length=200)