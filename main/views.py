from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'main/home.html', {'active_page': 1})


def courses(request):
    courses_list = Course.objects.all()[:9]
    context = {
        'active_page': 2,
        'courses': courses_list,
    }
    return render(request, 'main/courses.html', context)