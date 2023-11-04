from django.urls import path , include
from .views import CategoryViewSet, InfoViewSet  #CategoryView
from rest_framework import routers



router = routers.DefaultRouter()

# router.register(r'' , CategoryView , 'items' )
# Register the viewsets with the router
router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'info', InfoViewSet)


urlpatterns = [
    path('' , include(router.urls))
]


