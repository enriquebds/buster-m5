from rest_framework.views import APIView, Request, Response, status
from .serializers import UserSerializer, LoginSerializer
from .models import User
from django.contrib.auth import authenticate

class RegisterView(APIView):
    
    def post(self, req: Request) -> Response:
        serializer = UserSerializer(data=req.data)

        serializer.is_valid(raise_exception=True)
        
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

class LoginView(APIView):
    
    def post(self, req: Request) -> Response:
        serializer = LoginSerializer(data=req.data)

        serializer.is_valid(raise_exception=True)
        
        user = authenticate(username=serializer.validated_data["username"], password=serializer.validated_data["password"])

        if not user:
            return Response({"detail": "No active account found with the given credentials"}, status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.data, status.HTTP_201_CREATED)
