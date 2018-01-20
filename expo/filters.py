from django import forms
from .models import *
import django_filters

class PaintingFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='contains')
    f_artist = django_filters.ModelMultipleChoiceFilter(queryset=Artist.objects.all().order_by('artist_name'), widget=forms.CheckboxSelectMultiple)
    f_genre = django_filters.ModelMultipleChoiceFilter(queryset=Genre.objects.all().order_by('genre_title'), widget=forms.CheckboxSelectMultiple)
    f_period = django_filters.ModelMultipleChoiceFilter(queryset=Period.objects.all().order_by('period_title'), widget=forms.CheckboxSelectMultiple)
    f_artist__f_city__f_country = django_filters.ModelMultipleChoiceFilter(queryset=Country.objects.all().order_by('country_name'), widget=forms.CheckboxSelectMultiple)
    f_museum = django_filters.ModelMultipleChoiceFilter(queryset=Museum.objects.all().order_by('museum_title'), widget=forms.CheckboxSelectMultiple)
    rating = django_filters.NumberFilter()
    created_date = django_filters.NumberFilter(lookup_expr='year')
    published_date = django_filters.DateFilter()

    class Meta:
        model = Painting
        fields = ['title', 'f_artist', 'f_genre', 'f_period', 'f_artist__f_city__f_country', 'f_museum', 'rating', 'created_date', 'published_date', ]