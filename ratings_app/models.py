from django.db import models

# Create your models here.

class Rater(models.Model):
    user_id = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=3, null=True)
    occupation = models.CharField(max_length=20, null=True)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.occupation


class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    release_date = models.CharField(max_length=30)
    video_release = models.CharField(max_length=30, default="")
    imdb_url = models.CharField(max_length=400)
    unknown = models.IntegerField()
    action = models.IntegerField()
    adventure = models.IntegerField()
    animation = models.IntegerField()
    children = models.IntegerField()
    comedy = models.IntegerField()
    crime = models.IntegerField()
    documentary = models.IntegerField()
    drama = models.IntegerField()
    fantasy = models.IntegerField()
    film_noir = models.IntegerField()
    horror = models.IntegerField()
    musical = models.IntegerField()
    mystery = models.IntegerField()
    romance = models.IntegerField()
    sci_fi = models.IntegerField()
    thriller = models.IntegerField()
    war = models.IntegerField()
    western = models.IntegerField()

    def __str__(self):
        return self.title


class Rating(models.Model):
        user_id = models.ForeignKey(Rater)
        item_id = models.ForeignKey(Movie)
        rating = models.IntegerField()
        timestamp = models.IntegerField()

        def __str__(self):
            return self.rating