from rest_framework import serializers
from .models import *


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = '__all__'

    def get_movies_count(self, director):
        return director.movies_count


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"

    def get_reviews(self, movie):
        return [review.stars for review in movie.reviews.all()]

    def get_rating(self, movie):
        return movie.rating


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=100)
    description = serializers.CharField(min_length=1)
    duration = serializers.IntegerField(min_value=1)
    director_id = serializers.IntegerField(min_value=1)


class MovieDetailValidateSerializer(MovieValidateSerializer):
    pass


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=2)
    movie_id = serializers.IntegerField(min_value=1)


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)