
from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=140)
    address = models.CharField(max_length=140)
    city = models.CharField(max_length=140)
    zip_code = models.CharField(max_length=140)
    email = models.CharField(max_length=140)
    hashpw = models.CharField(max_length=140)

    def __str___(self):
        return self.name
    
