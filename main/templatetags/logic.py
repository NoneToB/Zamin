from django import template
from ..models import Course, LessonCompletion, LastLesson
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.filter
def is_enrolled(course_id, user_id):
    course = Course.objects.get(pk=course_id)
    return course.users.filter(user_id=user_id).exists()


@register.filter
def is_completed(lesson, user_id):
    return LessonCompletion.objects.filter(lesson=lesson, user_id=user_id).exists()


@register.filter
def is_last(lesson, user_id):
    try:
        last = LastLesson.objects.get(course=lesson.course, user=user_id)
        return lesson == last.next_lesson
    except:
        return False
