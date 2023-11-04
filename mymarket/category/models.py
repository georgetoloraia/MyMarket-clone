from django.db import models
from childcategory.models import ChildCategory



# class Category(models.Model):
#     name = models.CharField(max_length=150)
#     childcategory = models.ForeignKey(ChildCategory , on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name




class Category(models.Model):
    nadzvisxe = models.CharField(max_length=255)
    texnika = models.CharField(max_length=255)
    iaragi = models.CharField(max_length=255)

class Info(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    telnumber = models.CharField(max_length=255)
    images = models.ImageField(upload_to='info_images/', blank=True, null=True)
    mdebareoba = models.CharField(max_length=255)
    text = models.TextField()
    salary = models.IntegerField()
