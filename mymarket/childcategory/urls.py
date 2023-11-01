from django.urls import path , include
from .views import  ChildCategoryView
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'' , ChildCategoryView , 'items' )


urlpatterns = [
    path('' , include(router.urls))
]


