from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
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
    course_slug = Course.objects.get(id=course_id).slug
    return redirect('course-detail', course_slug)


@login_required
def lesson_view(request, course_slug, lesson_slug=None):
    context = {}

    course = get_object_or_404(Course, slug=course_slug)
    if not course.users.filter(pk=request.user.pk).exists():
        redirect('course-detail', course.slug)

    last_lesson, last_lesson_created = LastLesson.objects.get_or_create(course=course, user=request.user)
    context['last_lesson'] = last_lesson

    if not lesson_slug:
        return redirect('lesson-view', course.slug, last_lesson.last_lesson.slug)

    lesson = get_object_or_404(Lesson, slug=lesson_slug)
    if lesson.course.slug != course_slug:
        return redirect('course-detail', lesson.course.slug)
    context['current_lesson'] = lesson

    # is lesson accessible by user
    if hasattr(last_lesson, 'next_lesson') and last_lesson.next_lesson:
        last_lesson_obj = LastLesson.objects.get(course=course, user=request.user)
        if lesson.order_number > last_lesson_obj.next_lesson.order_number:
            return redirect('lesson-view', course.slug, last_lesson_obj.last_lesson.next_lesson.slug)
    elif lesson != course.lessons.first():
        return redirect('lesson-view', course.slug, course.lessons.first().slug)

    context['course'] = course

    return render(request, 'lesson/base.html', context)


@login_required
def complete_lesson(request, course_slug, lesson_slug):
    try:
        course = Course.objects.get(slug=course_slug)
    except ObjectDoesNotExist:
        return Http404("Course Doesn't exist")

    try:
        lesson = course.lessons.get(slug=lesson_slug)
    except ObjectDoesNotExist:
        return redirect('lesson-view', course_slug)

    LessonCompletion.objects.get_or_create(lesson=lesson, user=request.user)
    last_lesson_obj, created = LastLesson.objects.get_or_create(course=course, user=request.user)
    last_lesson_obj.last_lesson = lesson
    last_lesson_obj.save()
    print(lesson.next_lesson)
    if lesson.next_lesson:
        redirect_slug = lesson.next_lesson.slug
    else:
        redirect_slug = lesson.slug
    return redirect('lesson-view', course.slug, redirect_slug)


def handler404(request, *args, **kwargs):
    response = render(request, 'index.html')
    response.status_code = 404
    return response
