from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
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
    course = Course.objects.get(slug__exact=course_slug)
    is_enrolled = False
    if request.user.is_authenticated:
        user = request.user
        is_enrolled = Enrollment.objects.filter(user=user, course=course).exists()
    context = {
        'course': course,
        'is_enrolled': is_enrolled,
    }
    return render(request, 'main/course-detail.html', context)


@login_required
def enroll_course(request, course_id):
    enrollment = Enrollment.objects.get_or_create(user=request.user, course_id=course_id)
    enrollment.save()
    course_slug = Course.objects.get(id=course_id).slug
    return redirect('course-detail', course_slug)


@login_required
def lesson_view(request, course_slug, lesson_slug=None):
    context = {}
    if lesson_slug:
        lesson = get_object_or_404(Lesson, slug=lesson_slug)
        if lesson.course.slug != course_slug:
            return redirect('course-detail', lesson.course.slug)
        context['current_lesson'] = lesson
    course = get_object_or_404(Course, slug=course_slug)

    if not course.users.filter(pk=request.user.pk).exists():
        redirect('course-detail', course.slug)

    context['course'] = course
    return render(request, 'lesson/base.html', context)
