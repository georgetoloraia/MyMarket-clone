from django.db import models
from childcategory.models import ChildCategory



class Category(models.Model):
    name = models.CharField(max_length=150)
    childcategory = models.ForeignKey(ChildCategory , on_delete=models.CASCADE)

    def __str__(self):
        return self.name



