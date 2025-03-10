from django.contrib import admin
from account.models import User, BlockIpAddress

# Register your models here.

admin.site.register(User)
admin.site.register(BlockIpAddress)