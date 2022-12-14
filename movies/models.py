from django.db import models

from users.models import User


class Categories(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True)
    rating = models.CharField(max_length=20, choices=Categories.choices, default=Categories.G)
    synopsis = models.TextField(null=True)
    
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movies"
    )

    users_buyers = models.ManyToManyField(
        User, related_name="movies_bought")



class MovieOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)