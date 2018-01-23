from django import forms
from .models import *
import django_filters

# RATING_CHOICES
class PaintingFilter(django_filters.FilterSet):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    title = django_filters.CharFilter(lookup_expr='icontains')
    f_artist = django_filters.ModelMultipleChoiceFilter(queryset=Artist.objects.all().order_by('artist_name'), widget=forms.CheckboxSelectMultiple)
    f_genre = django_filters.ModelMultipleChoiceFilter(queryset=Genre.objects.all().order_by('genre_title'), widget=forms.CheckboxSelectMultiple)
    f_period = django_filters.ModelMultipleChoiceFilter(queryset=Period.objects.all().order_by('period_title'), widget=forms.CheckboxSelectMultiple)
    f_artist__f_city__f_country = django_filters.ModelMultipleChoiceFilter(queryset=Country.objects.all().order_by('country_name'), widget=forms.CheckboxSelectMultiple)
    f_museum = django_filters.ModelMultipleChoiceFilter(queryset=Museum.objects.all().order_by('museum_title'), widget=forms.CheckboxSelectMultiple)
    rating_gte = django_filters.ChoiceFilter(name='rating', choices=RATING_CHOICES, lookup_expr='gte')
    rating_lte = django_filters.ChoiceFilter(name='rating', choices=RATING_CHOICES, lookup_expr='lte')
    created_year_gte = django_filters.NumberFilter(name='created_year', lookup_expr='gte')
    created_year_lte = django_filters.NumberFilter(name='created_year', lookup_expr='lte')
    published_date_gte = django_filters.DateFilter(name='published_date', lookup_expr='gte')
    published_date_lte = django_filters.DateFilter(name='published_date', lookup_expr='lte')


    class Meta:
        model = Painting
        fields = ['title', 'f_artist', 'f_genre', 'f_period', 'f_artist__f_city__f_country', 'f_museum', 'rating', 'created_year', 'published_date', ]