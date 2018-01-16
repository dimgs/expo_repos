from django.db import models
from django.utils import timezone



class Period(models.Model):
    period_title = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.period_title




class Country(models.Model):
    country_name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.country_name




class City(models.Model):
    f_country = models.ForeignKey(Country, default='0', on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.city_name




class Museum(models.Model):
    f_city = models.ForeignKey(City, default='0', on_delete=models.CASCADE)
    museum_title = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.museum_title




class Genre(models.Model):
    genre_title = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.genre_title




class Artist(models.Model):
    f_city = models.ForeignKey(City, default='0', on_delete=models.CASCADE)
    artist_name = models.CharField(max_length=100)

    def __str__(self):
        return self.artist_name




class Painting(models.Model):
    f_artist = models.ForeignKey(Artist, default='0', on_delete=models.CASCADE)
    f_genre = models.ForeignKey(Genre, default='0', on_delete=models.CASCADE)
    f_period = models.ForeignKey(Period, default='0', on_delete=models.CASCADE)
    f_museum = models.ForeignKey(Museum, default='0', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    art_image = models.ImageField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    counter_popularity = models.IntegerField(default=0, blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#*********************************************************************************

