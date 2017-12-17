from django.shortcuts import render, get_object_or_404
from .models import Painting


def painting_list(request):
    paint_objects = Painting.objects.all().order_by('artist')
    return render(request, 'expo/painting_list.html', {'paint_objects': paint_objects})


def painting_detail(request, pk):
    paint_object = get_object_or_404(Painting, pk=pk)
    return render(request, 'expo/painting_detail.html', {'paint_object': paint_object})