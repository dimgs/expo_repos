from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.db.models import Q
from expo.models import *

########################################################################################################################

def gallery(request, null=None):
    artist_ID = request.GET.get('artist_id', '')
    genre_ID = request.GET.get('genre_id', '')
    museum_ID = request.GET.get('museum_id', '')
    period_ID = request.GET.get('period_id', '')
    artist_city_ID = request.GET.get('artist_city_id', '')
    artist_country_ID = request.GET.get('artist_country_id', '')
    museum_city_ID = request.GET.get('museum_city_id', '')
    museum_country_ID = request.GET.get('museum_country_id', '')
    txt = request.GET.get('txt', '')  # Search field text

    try:
        artist_ID = int(artist_ID)
    except:
        artist_ID = False

    try:
        genre_ID = int(genre_ID)
    except:
        genre_ID = False

    try:
        museum_ID = int(museum_ID)
    except:
        museum_ID = False

    try:
        period_ID = int(period_ID)
    except:
        period_ID = False

    try:
        artist_city_ID = int(artist_city_ID)
    except:
        artist_city_ID = False

    try:
        artist_country_ID = int(artist_country_ID)
    except:
        artist_country_ID = False

    try:
        museum_city_ID = int(museum_city_ID)
    except:
        museum_city_ID = False

    try:
        museum_country_ID = int(museum_country_ID)
    except:
        museum_country_ID = False


    if (artist_ID == False) and (genre_ID == False) and (museum_ID == False) and (period_ID == False) and (artist_city_ID == False) and (artist_country_ID == False) and (museum_city_ID == False) and (museum_country_ID == False):
       #if-else for "Search button"
       if (txt == ''):
           paint_objects = Painting.objects.all().order_by('title')
       else:
           paint_objects = Painting.objects.filter(Q(title__contains = txt) | Q(description__contains = txt) |
                                                   Q(f_artist__artist_name__contains = txt) | Q(f_genre__genre_title__contains = txt) |
                                                   Q(f_period__period_title__contains = txt) | Q(f_museum__museum_title__contains = txt) |
                                                   Q(f_artist__f_city__city_name__contains = txt) | Q(f_museum__f_city__city_name__contains = txt) |
                                                   Q(f_museum__museum_title__contains = txt)).order_by('title')
    elif artist_ID != False:
        paint_objects = Painting.objects.filter(f_artist = artist_ID).order_by('title')
    elif genre_ID != False:
        paint_objects = Painting.objects.filter(f_genre = genre_ID).order_by('title')
    elif museum_ID != False:
        paint_objects = Painting.objects.filter(f_museum = museum_ID).order_by('title')
    elif period_ID != False:
        paint_objects = Painting.objects.filter(f_period = period_ID).order_by('title')
    elif artist_city_ID != False:
        paint_objects = Painting.objects.filter(f_artist__f_city = artist_city_ID).order_by('title')
    elif artist_country_ID != False:
        paint_objects = Painting.objects.filter(f_artist__f_city__f_country = artist_country_ID).order_by('title')
    elif museum_city_ID != False:
        paint_objects = Painting.objects.filter(f_museum__f_city = museum_city_ID).order_by('title')
    elif museum_country_ID != False:
        paint_objects = Painting.objects.filter(f_museum__f_city__f_country = museum_country_ID).order_by('title')

    #Artist distinct
    artists_distinct = Artist.objects.all().distinct().order_by('artist_name')

    #Genres distinct
    genres_distint = Genre.objects.all().distinct().order_by('genre_title')

    #Periods distinct
    periods_distinct = Period.objects.all().distinct().order_by('period_title')

    #Countries distinct
    countries_distinct = Country.objects.all().distinct().order_by('country_name')

    #Museums distinct
    museums_distinct = Museum.objects.all().distinct().order_by('museum_title')

    return render(request, 'expo/gallery.html', locals())

########################################################################################################################

def painting_detail(request, pk):
    paint_object = get_object_or_404(Painting, pk=pk)
    return render(request, 'expo/painting_detail.html', {'paint_object': paint_object})

########################################################################################################################

def index(request):
    return render(request, 'expo/index.html', {})

########################################################################################################################

def contact(request):
    return render(request, 'expo/contact.html', {})

########################################################################################################################

def museums(request):
    uk_museums = Museum.objects.filter(f_city__f_country__country_name__contains="United Kingdom")
    london_museums = Museum.objects.filter(f_city__city_name__contains="London")
    return render(request, 'expo/museums.html', locals())

########################################################################################################################

def cities(request):
    greek_cities = City.objects.filter(f_country__country_name__contains="Greece")
    return render(request, 'expo/cities.html', locals())

########################################################################################################################
'''
def annotate_genres(request):
    genres_annotate = Genre.objects.annotate(number_of_entries=Count('painting'))
    return render(request, 'expo/annotate_genres.html', locals())
'''
########################################################################################################################






















