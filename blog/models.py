from django.db import models

# Create your models here.

class  Blog(models.Model):
    tittle=models.CharField(max_length=200)
    describtion=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.tittle
