from django.db import models

# Create your models here.

class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Subscribe(AbstractModel):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, unique=True)
    
    
    def __str__(self):
        return self.email
    


class Test(models.Model):
    title = models.CharField(max_length=100, null=True, unique=True, blank=True)
    num = models.CharField(max_length=50, unique=True)



class Contact(AbstractModel):
    first_name = models.CharField('First name', max_length=200)
    last_name = models.CharField('Last name', max_length=200, null=True, blank=True)
    email = models.EmailField('Email', max_length=200)
    message = models.TextField('Message')

    def __str__(self):
        return self.first_name