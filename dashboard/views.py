from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    context = {
        'active_page': 3,
        'active_section': 'home',
    }
    return render(request, 'dashboard/base.html', context)


@login_required
def my_profile(request):
    context = {
        'active_page': 3,
        'active_section': 'my_profile',
    }
    return render(request, 'dashboard/base.html', context)


@login_required
def my_courses(request):
    context = {
        'active_page': 3,
        'active_section': 'my_courses',
    }
    return render(request, 'dashboard/base.html', context)


@login_required
def saved_courses(request):
    context = {
        'active_page': 3,
        'active_section': 'saved_courses',
    }
    return render(request, 'dashboard/base.html', context)


@login_required
def comments(request):
    context = {
        'active_page': 3,
        'active_section': 'comments',
    }
    return render(request, 'dashboard/base.html', context)


@login_required
def my_test_attempts(request):
    context = {
        'active_page': 3,
        'active_section': 'my_test_attempts',
    }
    return render(request, 'dashboard/base.html', context)
