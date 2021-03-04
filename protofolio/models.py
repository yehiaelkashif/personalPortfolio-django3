from django.db import models

# Create your models here.
class  project(models.Model):
    tittle=models.CharField(max_length=100)
    describtion=models.CharField(max_length=250)
    image=models.ImageField(upload_to="protofolio/images/")
    url=models.URLField(blank=True)
    def __str__(self):
        return self.tittle
