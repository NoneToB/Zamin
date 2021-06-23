from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html', {'active_page': 1})


def courses(request):
    context = {
        'active_page': 2,
    }
    return render(request, 'main/courses.html', context)