from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# from items.models import Item

class Category(MPTTModel):
    name = models.CharField(max_length=150 , help_text='Enter the name of the category.')
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return self.name
    

    
    class MPTTMeta:
            order_insertion_by = ['name']
