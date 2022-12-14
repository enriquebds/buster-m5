from rest_framework.views import APIView, Request, Response, status
from .serializers import UserSerializer, LoginSerializer
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import Permission

class RegisterView(APIView):
    
    def post(self, req: Request) -> Response:
        serializer = UserSerializer(data=req.data)

        serializer.is_valid(raise_exception=True)
        
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

class LoginView(TokenObtainPairView):
    ...
    
class UserDetailView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [Permission]
    

    def get(self, request: Request, user_id: int) -> Response:
        user = User.objects.get(id=user_id)
        self.check_object_permissions(request,user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK) 