from django.contrib import admin
from django.urls import path, include
from .views import UserCreateView , CurrentUserView  #, CustomLoginView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('items.urls')),
    path('perent/', include('category.urls')),
    path('child/', include('childcategory.urls')),
    path('users/' , UserCreateView.as_view(), name='user-create' ),
    path('login/' , obtain_auth_token, name='login'),
    path('users/me' , CurrentUserView.as_view() , name='current-user'),

]


