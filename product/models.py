from django.db import models

class Product(models.Model):
  menu = models.CharField(max_length=255)
  price = models.CharField(max_length=255)