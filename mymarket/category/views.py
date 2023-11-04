# from django.shortcuts import render
# from rest_framework import viewsets
# from .serializers import  CategorySerializer 
# from .models import  Category 



# class CategoryView(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


from rest_framework import viewsets, filters

from .filters import CategoryFilter, InfoFilter
from .models import Category, Info
from .serializers import CategorySerializer, InfoSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = CategoryFilter

class InfoViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = InfoFilter



