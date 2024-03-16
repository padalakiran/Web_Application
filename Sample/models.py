from django.db import models


# Create your models here.
class sd(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()  # Corrected field name to 'email'
    age = models.IntegerField()
    DateOfBirth = models.DateField()
