from rest_framework.views import APIView, Request, Response, status
from rest_framework.permissions import IsAuthenticated
from .serializers import MovieOrderSerializer, MovieSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from movies.permissions import IsEmployee
from _core.pagination import CustomLimitOffsetPagination
from .models import Movie
from django.shortcuts import get_object_or_404


class MovieView(APIView, CustomLimitOffsetPagination):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployee]
    
    def post(self, req: Request) -> Response:
        serializer = MovieSerializer(data=req.data)

        serializer.is_valid(raise_exception=True)
        
        serializer.save(user=req.user)

        return Response(serializer.data, status.HTTP_201_CREATED)
        

    def get(self, req: Request) -> Response:
        movies = Movie.objects.all()
        pages = self.paginate_queryset(movies, req, view=self)
        serializer = MovieSerializer(pages, many=True)

        return self.get_paginated_response(serializer.data)

class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployee]

    def get(self, req: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)

        serializer = MovieSerializer(movie)

        return Response(serializer.data, status.HTTP_200_OK)
        

    def delete(self, req: Request, movie_id: int) -> Response:

        movie = get_object_or_404(Movie, id=movie_id)
        
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class MovieOrderDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, req, movie_id) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        movie_order= MovieOrderSerializer(data=req.data)
        movie_order.is_valid(raise_exception=True)
        movie_order.save(user_order=req.user, movie_order=movie)
        return Response(movie_order.data, status.HTTP_201_CREATED)
