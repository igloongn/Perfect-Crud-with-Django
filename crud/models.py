from email.policy import default
from django.db import models

# Create your models here.
class UserModel(models.Model):
    firstname=models.CharField(max_length=20, null=True, blank=True)
    lastname=models.CharField(max_length=20, null=True, blank=True)
    photo=models.ImageField(default="This is a default Photo")
    time=models.TimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.firstname
        