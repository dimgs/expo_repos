from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField
from django.core.validators import MinValueValidator, MaxValueValidator



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



STATUS_CHOICES=(
    ('online', 'On'),
    ('offline', 'Off')
)

class Painting(models.Model):
    f_artist = models.ForeignKey(Artist, default='0', on_delete=models.CASCADE)
    f_genre = models.ForeignKey(Genre, default='0', on_delete=models.CASCADE)
    f_period = models.ForeignKey(Period, default='0', on_delete=models.CASCADE)
    f_museum = models.ForeignKey(Museum, default='0', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)], blank=True, null=True)
    art_image = models.ImageField(blank=True, null=True)
    created_year = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(2018)], blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    counter_popularity = models.PositiveIntegerField(default=0, blank=True, null=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='on')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title




class Famous(models.Model):
    FAMOUS_CHOICES = (
        ('Mona Lisa', 'Mona Lisa'),
        ('Starry Night', 'Starry Night'),
        ('The Last Supper', 'The Last Supper'),
        ('The Creation of Adam', 'The Creation of Adam'),
        ('Guernica', 'Guernica'),
    )
    title = MultiSelectField(choices=FAMOUS_CHOICES)