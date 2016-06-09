# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-08 07:34
from __future__ import unicode_literals

from django.db import migrations

import csv


def rating_stat(apps, schema_editor):
    Rater = apps.get_model("ratings_app", "Rater")
    Movie = apps.get_model("ratings_app", "Movie")
    Rating = apps.get_model("ratings_app", "Rating")

    with open("u.data") as outfile:
        rating = csv.DictReader(outfile, fieldnames=["user_id", "item_id",
                                "rating", "timestamp"], delimiter="\t")

        for row in rating:
            print(row)
            user_id = Rater.objects.get(user_id=row['user_id'])
            item_id = Movie.objects.get(movie_id=int(row['item_id']))
            rating = int(row['rating'])
            timestamp = int(row['timestamp'])

            def __str__(self):
                return str(self.rating)



class Migration(migrations.Migration):

    dependencies = [
        ('ratings_app', '0003_auto_20160608_0637'),
    ]

    operations = [
        migrations.RunPython(rating_stat)
    ]
