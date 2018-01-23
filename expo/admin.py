from django.contrib import admin
from .models import *


class PeriodAdmin(admin.ModelAdmin):
    list_display = ('period_title', 'id')
    search_fields = ('period_title', 'id')
admin.site.register(Period, PeriodAdmin)


class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_name', 'id')
    search_fields = ('country_name', 'id')
admin.site.register(Country, CountryAdmin)


class CityAdmin(admin.ModelAdmin):
        list_display = ('city_name', 'id', 'f_country')
        search_fields = ('city_name', 'id')
admin.site.register(City, CityAdmin)


class MuseumAdmin(admin.ModelAdmin):
    list_display = ('museum_title', 'id', 'f_city')
    search_fields = ('museum_title', 'id')
admin.site.register(Museum, MuseumAdmin)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre_title', 'id')
    search_fields = ('genre_title', 'id')
admin.site.register(Genre, GenreAdmin)


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('artist_name', 'id', 'f_city')
    search_fields = ('artist_name', 'id')
admin.site.register(Artist, ArtistAdmin)

######################################################

def on(modeladmin,request, queryset):
    queryset.update(status='online')

def off(modeladmin, request, queryset):
    queryset.update(status='offline')

class PaintingAdmin(admin.ModelAdmin):
    list_display = ('title', 'f_artist', 'f_genre', 'f_period', 'f_museum', 'published_date', 'counter_popularity', 'status', 'id')
    list_filter = ('status', 'f_genre', 'f_period', 'published_date', 'created_year', 'rating')
    search_fields = ('title', 'description')
    actions = [on, off]
admin.site.register(Painting, PaintingAdmin)

#######################################################

admin.site.register(Famous)