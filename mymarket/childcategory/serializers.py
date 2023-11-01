from rest_framework import serializers
from .models import ChildCategory



class ChildCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildCategory
        fields = "__all__"