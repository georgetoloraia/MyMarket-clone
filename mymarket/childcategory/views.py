from .models import ChildCategory
from .serializers import ChildCategorySerializer
from rest_framework import viewsets


class ChildCategoryView(viewsets.ModelViewSet):
    queryset = ChildCategory.objects.all()
    serializer_class = ChildCategorySerializer