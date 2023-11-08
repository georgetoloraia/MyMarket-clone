from django.contrib import admin
from django.urls import path, include
from .views import UserCreateView , CurrentUserView , UserListView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions



urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', include('items.urls')),
    path('category/', include('category.urls')),
    path('users/' , UserCreateView.as_view(), name='user-create' ),
    path('users/list/' , UserListView.as_view(), name="user's list"), 
    path('login/' , obtain_auth_token, name='login'),
    path('users/me' , CurrentUserView.as_view() , name='current-user'),

]


