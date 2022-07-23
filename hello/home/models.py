from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField(null=True)

class details(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    phone = models.CharField(max_length=12)
    add = models.TextField(max_length=150)
    def __str__(self):
        return self.name
class lgin(models.Model):
    EMAIL=models.EmailField(max_length=122)
    Password=models.CharField(max_length=18)