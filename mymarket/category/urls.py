from django.urls import path , include
from .views import  CategoryView
from rest_framework import routers



router = routers.DefaultRouter()

router.register(r'' , CategoryView , 'category' )


urlpatterns = [
    path('' , include(router.urls))
]


