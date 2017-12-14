from django.shortcuts import render


def painting_list(request):
    return render(request, 'expo/painting_list.html', {})