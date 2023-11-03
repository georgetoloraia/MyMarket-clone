from django.db import models 
from django.contrib.auth.models import User
from category.models import Category



class Item(models.Model):
    title = models.CharField(max_length=250)
    desctiption = models.CharField(max_length=500)
    price = models.CharField(max_length=100 )
    specifications = models.BooleanField(default=False) 
    mobile = models.CharField(max_length=200)
    user = models.ForeignKey(User , related_name='item' , on_delete=models.CASCADE )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    image = models.ImageField(upload_to='item_images/', blank=True , null=True)
    views = models.ManyToManyField(User, related_name='viewed_items', blank=True)


    def __str__(self):
        return self.title
    
    def num_views(self):
        return self.views.count()



# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     service = models.CharField(max_length=250)
#     rent = models.CharField(max_length=250)
#     house_and_garden = models.CharField(max_length=250)
#     techmic = models.CharField(max_length=250)
#     hunting_and_fishing = models.CharField(max_length=250)
#     music = models.CharField(max_length=250)
#     children = models.CharField(max_length=250)
