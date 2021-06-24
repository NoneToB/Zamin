from django.shortcuts import render
from .models import *


def home(request):
    return render(request, 'main/home.html', {'active_page': 1})


def courses(request):
    courses_list = Course.objects.all()[:9]
    categories = Category.objects.all()
    difficulties = Difficulty.objects.all()
    context = {
        'active_page': 2,
        'courses': courses_list,
        'categories': categories,
        'difficulties': difficulties,
    }
    return render(request, 'main/courses.html', context)


def course_detail(request, course_slug):
    courses()
    context = {}
    return render(request, 'main/course-detail.html', context)
