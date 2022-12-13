# Generated by Django 4.1.4 on 2022-12-13 09:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("movies", "0003_alter_movie_users_buyers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="users_buyers",
            field=models.ManyToManyField(
                related_name="movies_bought",
                through="movies.MovieOrder",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
