from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=150)

    @property
    def movies_count(self):
        return self.movies.all().count()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.FloatField(default=0)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    @property
    def rating(self):
        count = self.reviews.all().count()
        stars = sum([i.stars for i in self.reviews.all()])
        return stars // count if count > 0 else 0

    def __str__(self):
        return self.title

    @property
    def director_name(self):
        return self.director.name


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(choices=([i, i * '*'] for i in range(1, 6)), default=0)

    def __str__(self):
        return self.text









