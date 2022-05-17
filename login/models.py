from django.db import models
from django import forms
# Create your models here.

class user_data(models.Model):
    username = models.CharField(max_length=15)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    email = models.EmailField( max_length=254)
    # password = models.CharField(max_length=30,null=False)
    # date = models.DateField()
    # created_at = models.DateTimeField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    # created_at = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    # updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    # date = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        
        return self.username    