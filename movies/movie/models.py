from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=200)
    rating = models.FloatField(default=0)

    def __str__(self):
        return f'{self.name} {self.rating}'
