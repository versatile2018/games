from django.db import models

# Create your models here.

class login(models.Model):
    username = models.CharField(max_length=200)
    password = models.TextField(max_length=200)


