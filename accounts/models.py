from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager , User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile")
    profile_picture = models.ImageField(upload_to='pics/',default="pics/aks.jpg")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    address=models.TextField(default="12")
    man=1
    woman=2
    status_choices=((man,"man"),(woman,"woman"))
    Gender=models.IntegerField(choices=status_choices , default=man)


    def __str__(self):
        return self.user.username