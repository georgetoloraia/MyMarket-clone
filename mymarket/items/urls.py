from django.urls import path , include
from .views import ItemView 
from rest_framework import routers



router = routers.DefaultRouter()

router.register(r'' , ItemView , 'items' )


urlpatterns = [
    path('' , include(router.urls))
]


