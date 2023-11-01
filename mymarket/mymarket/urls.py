from django.contrib import admin
from django.urls import path, include
from .views import UserCreateView , CurrentUserView  #, CustomLoginView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions


from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
    openapi.Info(
        title="Your API Title",
        default_version="v1",
        description="Your API description",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('items.urls')),
    path('perent/', include('category.urls')),
    path('child/', include('childcategory.urls')),
    path('users/' , UserCreateView.as_view(), name='user-create' ),
    path('login/' , obtain_auth_token, name='login'),
    path('users/me' , CurrentUserView.as_view() , name='current-user'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]


