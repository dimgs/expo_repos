from django.shortcuts import render
from .models import Painting


def painting_list(request):
    paintings = Painting.objects.all().order_by('artist')
    return render(request, 'expo/painting_list.html', {'paintings': paintings})