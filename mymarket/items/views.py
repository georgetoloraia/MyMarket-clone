from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ItemSerializer 
from .models import Item 

class ItemView(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Item.objects.filter(user=user)
        else:
            return Item.objects.none() 
        


class ItemListView(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
