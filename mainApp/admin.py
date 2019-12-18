from django.contrib import admin
from .models import UserProfileInfo, UserToken, PasswordToken

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(UserToken)
admin.site.register(PasswordToken)
