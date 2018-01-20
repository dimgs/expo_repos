from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from expo.models import *
from .filters import PaintingFilter

########################################################################################################################
###################### Gallery ###########################

def gallery(request, null=None):
    artist_id = request.GET.get('artist_id', '')
    genre_id = request.GET.get('genre_id', '')
    museum_id = request.GET.get('museum_id', '')
    period_id = request.GET.get('period_id', '')
    artist_city_id = request.GET.get('artist_city_id', '')
    artist_country_id = request.GET.get('artist_country_id', '')
    museum_city_id = request.GET.get('museum_city_id', '')
    museum_country_id = request.GET.get('museum_country_id', '')
    txt = request.GET.get('txt', '')  #Search text field
    order_status_date = request.GET.get('order_status_date', '')
    order_status_popularity = request.GET.get('order_status_popularity', '')
    order_status_rating = request.GET.get('order_status_rating', '')
    complex_filters_status = request.GET.get('complex_filters_status', '')

    try:
        artist_id = int(artist_id)
    except:
        artist_id = False

    try:
        genre_id = int(genre_id)
    except:
        genre_id = False

    try:
        museum_id = int(museum_id)
    except:
        museum_id = False

    try:
        period_id = int(period_id)
    except:
        period_id = False

    try:
        artist_city_id = int(artist_city_id)
    except:
        artist_city_id = False

    try:
        artist_country_id = int(artist_country_id)
    except:
        artist_country_id = False

    try:
        museum_city_id = int(museum_city_id)
    except:
        museum_city_id = False

    try:
        museum_country_id = int(museum_country_id)
    except:
        museum_country_id = False

    try:
        order_status_date = int(order_status_date)
    except:
        order_status_date = 'empty'

    try:
        order_status_rating = int(order_status_rating)
    except:
        order_status_rating = 'empty'

    try:
        order_status_popularity = int(order_status_popularity)
    except:
        order_status_popularity = 'empty'


#######################################################################################################################
################################## DICTIONARIES #################################

    #LOCAL VARIABLES "id" DICTIONARY
    var_dict = {'artist_id':artist_id, 'genre_id':genre_id, 'museum_id':museum_id, 'period_id':period_id,
                'artist_country_id':artist_country_id, 'museum_city_id':museum_city_id,
                'museum_country_id':museum_country_id }


    #FOREIGN KEYS & "id" DICTIONARY
    foreign_id_dict = { 'f_artist':artist_id, 'f_genre':genre_id, 'f_museum':museum_id, 'f_period':period_id,
                        'f_artist__f_city':artist_city_id, 'f_artist__f_city__f_country':artist_country_id,
                        'f_museum__f_city':museum_city_id, 'f_museum__f_city__f_country':museum_country_id }

#######################################################################################################################

    #Checking if all items of "var_dict"(variables dictionary) are FALSE
    for key, value in var_dict.items():
        if value == False:
            result_var_dict = False
        else:
            result_var_dict = True
            break

#######################################################################################################################
############################# SORTING ####################################

    #If all items of "var_dict"(variables dictionary) are FALSE
    if result_var_dict == False:
       #Search field without text
       if (txt == ''):
           #Order Status "Date" - Descending
            if order_status_date == 1:
                paint_objects = Painting.objects.all().order_by('-published_date')
                order_status_date = 0
            #Order Status "Date" - Ascending
            elif order_status_date == 0:
                paint_objects = Painting.objects.all().order_by('published_date')
                order_status_date = 1
            #Order Status "Popularity" - Descending
            elif order_status_popularity == 1:
                paint_objects = Painting.objects.all().order_by('-counter_popularity')
                order_status_popularity = 0
            #Order Status "Popularity" - Ascending
            elif order_status_popularity == 0:
                paint_objects = Painting.objects.all().order_by('counter_popularity')
                order_status_popularity = 1
            #Order Status "Rating" - Descending
            elif order_status_rating == 1:
                paint_objects = Painting.objects.all().order_by('-rating')
                order_status_rating = 0
            #Order Status "Rating" - Ascending
            elif order_status_rating == 0:
                paint_objects = Painting.objects.all().order_by('rating')
                order_status_rating = 1
            #With default Order
            else:
                paint_objects = Painting.objects.all().order_by('-published_date')

       #SEARCH FIELD with text entry
       else:
           #Order Status "Date" - Descending
            if order_status_date == 1:
                paint_objects = Painting.objects.filter(Q(title__contains=txt) | Q(description__contains=txt) |
                                                        Q(f_artist__artist_name__contains=txt) | Q(f_genre__genre_title__contains=txt) |
                                                        Q(f_period__period_title__contains=txt) | Q(f_museum__museum_title__contains=txt) |
                                                        Q(f_artist__f_city__city_name__contains=txt) | Q(f_museum__f_city__city_name__contains=txt) |
                                                        Q(f_museum__museum_title__contains=txt)).order_by('-published_date')
                order_status_date = 0
            #Order Status "Date" - Ascending
            elif order_status_date == 0:
                paint_objects = Painting.objects.filter(Q(title__contains=txt) | Q(description__contains=txt) |
                                                        Q(f_artist__artist_name__contains=txt) | Q(f_genre__genre_title__contains=txt) |
                                                        Q(f_period__period_title__contains=txt) | Q(f_museum__museum_title__contains=txt) |
                                                        Q(f_artist__f_city__city_name__contains=txt) | Q(f_museum__f_city__city_name__contains=txt) |
                                                        Q(f_museum__museum_title__contains=txt)).order_by('published_date')
                order_status_date = 1
            #Order Status "Popularity" - Descending
            elif order_status_popularity == 1:
                paint_objects = Painting.objects.filter(Q(title__contains=txt) | Q(description__contains=txt) |
                                                        Q(f_artist__artist_name__contains=txt) | Q(f_genre__genre_title__contains=txt) |
                                                        Q(f_period__period_title__contains=txt) | Q(f_museum__museum_title__contains=txt) |
                                                        Q(f_artist__f_city__city_name__contains=txt) | Q(f_museum__f_city__city_name__contains=txt) |
                                                        Q(f_museum__museum_title__contains=txt)).order_by('-counter_popularity')
                order_status_popularity = 0
            #Order Status "Popularity" - Ascending
            elif order_status_popularity == 0:
                paint_objects = Painting.objects.filter(Q(title__contains=txt) | Q(description__contains=txt) |
                                                        Q(f_artist__artist_name__contains=txt) | Q(f_genre__genre_title__contains=txt) |
                                                        Q(f_period__period_title__contains=txt) | Q(f_museum__museum_title__contains=txt) |
                                                        Q(f_artist__f_city__city_name__contains=txt) | Q(f_museum__f_city__city_name__contains=txt) |
                                                        Q(f_museum__museum_title__contains=txt)).order_by('counter_popularity')
                order_status_popularity = 1
            #Order Status "Rating" - Descending
            elif order_status_rating == 1:
                paint_objects = Painting.objects.filter(Q(title__contains=txt) | Q(description__contains=txt) |
                                                        Q(f_artist__artist_name__contains=txt) | Q(f_genre__genre_title__contains=txt) |
                                                        Q(f_period__period_title__contains=txt) | Q(f_museum__museum_title__contains=txt) |
                                                        Q(f_artist__f_city__city_name__contains=txt) | Q(f_museum__f_city__city_name__contains=txt) |
                                                        Q(f_museum__museum_title__contains=txt)).order_by('-rating')
                order_status_rating = 0
            #Order Status "Rating" - Ascending
            elif order_status_rating == 0:
                paint_objects = Painting.objects.filter(Q(title__contains=txt) | Q(description__contains=txt) |
                                                        Q(f_artist__artist_name__contains=txt) | Q(f_genre__genre_title__contains=txt) |
                                                        Q(f_period__period_title__contains=txt) | Q(f_museum__museum_title__contains=txt) |
                                                        Q(f_artist__f_city__city_name__contains=txt) | Q(f_museum__f_city__city_name__contains=txt) |
                                                        Q(f_museum__museum_title__contains=txt)).order_by('rating')
                order_status_rating = 1
            #With default Order
            else:
               paint_objects = Painting.objects.filter(Q(title__contains = txt) | Q(description__contains = txt) |
                                                       Q(f_artist__artist_name__contains = txt) | Q(f_genre__genre_title__contains = txt) |
                                                       Q(f_period__period_title__contains = txt) | Q(f_museum__museum_title__contains = txt) |
                                                       Q(f_artist__f_city__city_name__contains = txt) | Q(f_museum__f_city__city_name__contains = txt) |
                                                       Q(f_museum__museum_title__contains = txt)).order_by('-published_date')

    #If any item of "var_dict"(variables dictionary) has id number, e.g. artist_id = 1
    #Filtered paintings by "artist_id", "genre_id" etc. (by foreign_id_dict(foreign id dictionary) )
    else:
        for f_key, f_value in foreign_id_dict.items():
            #Checking if each value has id, e.g. artist_id = 1
            if f_value != False:
                # Order Status "Date" - Descending
                if order_status_date == 1:
                    #Example: f_key:f_value --> f_artist:artist_id
                    paint_objects = Painting.objects.filter( **{f_key:f_value} ).order_by('-published_date')
                    order_status_date = 0
                #Order Status "Date" - Ascending
                elif order_status_date == 0:
                     #Example: f_key:f_value --> f_artist:artist_id
                     paint_objects = Painting.objects.filter( **{f_key:f_value} ).order_by('published_date')
                     order_status_date = 1
                #Order Status "Popularity" - Descending
                elif order_status_popularity == 1:
                    #Example: f_key:f_value --> f_artist:artist_id
                    paint_objects = Painting.objects.filter( **{f_key:f_value} ).order_by('-counter_popularity')
                    order_status_popularity = 0
                #Order Status "Popularity" - Ascending
                elif order_status_popularity == 0:
                    #Example: f_key:f_value --> f_artist:artist_id
                    paint_objects = Painting.objects.filter( **{f_key:f_value} ).order_by('counter_popularity')
                    order_status_popularity = 1
                #Order Status "Rating" - Descending
                elif order_status_rating == 1:
                    #Example: f_key:f_value --> f_artist:artist_id
                    paint_objects = Painting.objects.filter( **{f_key:f_value} ).order_by('-rating')
                    order_status_rating = 0
                #Order Status "Rating" - Ascending
                elif order_status_rating == 0:
                    #Example: f_key:f_value --> f_artist:artist_id
                    paint_objects = Painting.objects.filter( **{f_key:f_value} ).order_by('rating')
                    order_status_rating = 1
                #With default Order
                else:
                    #Example: f_key:f_value --> f_artist:artist_id
                    paint_objects = Painting.objects.filter( **{f_key:f_value} ).order_by('title')


########################################################################################################################
#################### DISTINCT OBJECTS ####################

    #Artists distinct
    artists_distinct = Artist.objects.all().distinct().order_by('artist_name')

    #Genres distinct
    genres_distint = Genre.objects.all().distinct().order_by('genre_title')

    #Periods distinct
    periods_distinct = Period.objects.all().distinct().order_by('period_title')

    #Countries distinct
    countries_distinct = Country.objects.all().distinct().order_by('country_name')

    #Museums distinct
    museums_distinct = Museum.objects.all().distinct().order_by('museum_title')

    ########## Painting Filter by "filters.py" ##########
    painting_list = Painting.objects.all()
    painting_filter = PaintingFilter(request.GET, queryset=painting_list)

    ########## COMPLEX filters vs STANDARD filters #########
    if complex_filters_status != '':
        paint_objects = painting_filter.qs


    ### Return ###
    return render(request, 'expo/gallery.html', locals())

#######################################################################################################################



########################################################################################################################
############## Painting detail ##########################

def painting_detail(request, pk):
    paint_object = get_object_or_404(Painting, pk=pk)
    paint_object.counter_popularity = paint_object.counter_popularity + 1
    paint_object.save()
    return render(request, 'expo/painting_detail.html', {'paint_object': paint_object})

########################################################################################################################
############## Index ######################

def index(request):
    return render(request, 'expo/index.html', {})

########################################################################################################################
###################### Contact #######################

def contact(request):
    return render(request, 'expo/contact.html', {})

########################################################################################################################






















