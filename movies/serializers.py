from rest_framework import serializers
from .models import Movie, Categories

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False, allow_null=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, required=False, allow_null=True)
    rating = serializers.ChoiceField(choices=Categories.choices, default=Categories.G)
    synopsis = serializers.CharField(required=False, allow_null=True)
    added_by  = serializers.SerializerMethodField()
    

    def get_added_by(self, obj):
        return obj.user.email 


    def create(self, validated_data):
        return Movie.objects.create(**validated_data)