from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additionals
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', default=None, blank=True)

    def __str__(self):
        return self.user.username

User._meta.get_field('email')._unique = True


class UserToken(models.Model):
    token = models.CharField(max_length=37)
    link = models.URLField(blank=True)
    userId = models.IntegerField()

class PasswordToken(models.Model):
    token = models.CharField(max_length=37)
    link = models.URLField(blank=True)
    userId = models.IntegerField()