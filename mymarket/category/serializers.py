from rest_framework import serializers
from .models import Category 


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = "__all__"



from rest_framework import serializers

from .models import Category, Info

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'nadzvisxe', 'texnika', 'iaragi')

class InfoSerializer(serializers.ModelSerializer):
    images = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Info
        fields = ('id', 'category', 'telnumber', 'images', 'mdebareoba', 'text', 'salary')
