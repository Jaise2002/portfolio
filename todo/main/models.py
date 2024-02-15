from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
class mark(models.Model):
    mark1 = models.TextField(max_length=20)
    mark2 = models.TextField(max_length=20)
    mark3 = models.TextField(max_length=20)
    mark4 = models.TextField(max_length=20)