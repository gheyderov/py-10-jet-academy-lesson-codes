from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import AbstractModel

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def get_profile_image(self):
        if self.image:
            return self.image.url
        return '/static/images/profile.jpg/'


class UserAddress(AbstractModel):
    address = models.CharField('address', max_length=200)