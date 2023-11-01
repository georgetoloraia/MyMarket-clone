from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserCreateSerializer , UserSerializer 
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token



from rest_framework import permissions

class UnauthenticatedOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_authenticated


class UserCreateView(APIView):
    # permission_classes = [AllowAny]
    permission_classes = [UnauthenticatedOnly]
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"massage":'user created saccessfilly'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CurrentUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
